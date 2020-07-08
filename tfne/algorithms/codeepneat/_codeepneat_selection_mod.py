import math
import statistics


class CoDeepNEATSelectionMOD:
    def _select_modules_basic(self) -> ({int: int}, int, bool):
        """"""
        #### Offspring Size Calculation ####
        # Determine average fitness of each current species as well as the sum of each avg fitness
        mod_species_avg_fitness = dict()
        for spec_id, spec_mod_ids in self.mod_species.items():
            spec_avg_fitness = statistics.mean([self.modules[mod_id].get_fitness() for mod_id in spec_mod_ids])
            mod_species_avg_fitness[spec_id] = spec_avg_fitness
        total_avg_fitness = sum(mod_species_avg_fitness.values())

        # Calculate the amount of offspring assigned to each species based on the species share of the total avg fitness
        mod_species_offspring = dict()
        current_total_size = 0
        for spec_id, spec_avg_fitness in mod_species_avg_fitness.items():
            spec_size = math.floor((spec_avg_fitness / total_avg_fitness) * self.mod_pop_size)

            # Determine the assigned offspring size of the species, which is its determined size minus the modules
            # which will be preserved
            offspring_size = spec_size - self.mod_spec_mod_elitism
            if offspring_size <= self.mod_spec_min_offspring:
                offspring_size = self.mod_spec_min_offspring

            mod_species_offspring[spec_id] = offspring_size
            current_total_size += (offspring_size + self.mod_spec_mod_elitism)

        # If during math flooring operations and minimal offspring calculations the total size of the future species
        # deviates from the intended module size, adjust the offspring by removing offspring from the species with the
        # most assigned offspring or adding offspring by adding offspring to the species with least assigned offspring
        while current_total_size < self.mod_pop_size:
            min_spec_id = min(mod_species_offspring.keys(), key=mod_species_offspring.get)
            mod_species_offspring[min_spec_id] += 1
            current_total_size += 1
        while current_total_size > self.mod_pop_size:
            max_spec_id = max(mod_species_offspring.keys(), key=mod_species_offspring.get)
            mod_species_offspring[max_spec_id] -= 1
            current_total_size -= 1

        #### Module Selection ####
        for spec_id, spec_mod_ids in self.mod_species.items():
            # Sort module ids in species according to their fitness
            spec_mod_ids_sorted = sorted(spec_mod_ids, key=lambda x: self.modules[x].get_fitness(), reverse=True)

            # Determine module ids to remove in order to prevent to use them for reproduction
            removal_threshold_index = int(len(spec_mod_ids) * (1 - self.mod_spec_reprod_thres))
            # Correct removal index threshold if reproduction threshold so high that elitism modules would be removed
            if removal_threshold_index + self.mod_spec_mod_elitism < len(spec_mod_ids):
                removal_threshold_index = self.mod_spec_mod_elitism
            spec_mod_ids_to_remove = spec_mod_ids_sorted[removal_threshold_index:]

            # Delete low performing modules that will not be considered for reproduction from species assignment
            for mod_id_to_remove in spec_mod_ids_to_remove:
                self.mod_species[spec_id].remove(mod_id_to_remove)
                del self.modules[mod_id_to_remove]

        # Set reinit offspring to 0 and extinction to False, as no species can go extinct in basic selection
        reinit_offspring = 0
        pop_extinction = False
        return mod_species_offspring, reinit_offspring, pop_extinction

    def _select_modules_param_distance_fixed(self) -> ({int: int}, int, bool):
        """"""
        #### Determination of Species Extinction ####
        # Initialize counter of species elements that should be reinitialized upon species extinction
        reinit_offspring = 0

        # Determine average fitness of each current species and append it to the species avg fitness history
        for spec_id, spec_mod_ids in self.mod_species.items():
            spec_avg_fitness = statistics.mean([self.modules[mod_id].get_fitness() for mod_id in spec_mod_ids])
            if spec_id in self.mod_species_fitness_history:
                self.mod_species_fitness_history[spec_id].append(spec_avg_fitness)
            else:
                self.mod_species_fitness_history[spec_id] = [spec_avg_fitness]

        # Determine if species can be considered for extinction. Critera: Species existed long enough; species can be
        # removed according to species elitism; species is not the last of its module type. Then determine if species is
        # stagnating for the recent config specified time period (meaning that it had not improved at any time in the
        # recent time period). Preprocess current species by listing the frequency of module types as to not remove the
        # last species of a unique module type
        spec_type_frequency = dict()
        for mod_id in self.mod_species_repr.values():
            spec_mod_type = self.modules[mod_id].get_type()
            if spec_mod_type in spec_type_frequency:
                spec_type_frequency[spec_mod_type] += 1
            else:
                spec_type_frequency[spec_mod_type] = 1

        spec_ids_to_remove = list()
        for spec_id in self.mod_species:
            # Don't consider species for extinction if it hasn't existed long enough
            if len(self.mod_species_fitness_history[spec_id]) < self.mod_spec_max_stagnation:
                continue
            # Don't consider species for extinction if species elitism doesn't allow removal of further species
            if len(self.mod_species) <= self.mod_spec_species_elitism:
                continue
            # Don't consider species for extinction if it is the last of its module type and species elitism is set to
            # a value higher than all possible module types.
            spec_mod_type = self.modules[self.mod_species_repr[spec_id]].get_type()
            if spec_type_frequency[spec_mod_type] == 1 and self.mod_spec_species_elitism >= len(self.available_modules):
                continue

            # Consider species for extinction and determine if it has been stagnating
            distant_avg_fitness = self.mod_species_fitness_history[spec_id][-self.mod_spec_max_stagnation]
            recent_fitness_history = self.mod_species_fitness_history[spec_id][-self.mod_spec_max_stagnation:]
            if distant_avg_fitness >= max(recent_fitness_history):
                # Species is stagnating. Flag species to be removed later and decrement species type frequency
                spec_ids_to_remove.append(spec_id)
                species_type_frequency[species_mod_type] -= 1

        # Remove just determined species and species elements. If reinit_extinct flag activated, count how many species
        # memebers have gone extinct as this amount will be reinitialized later
        for spec_id in spec_ids_to_remove:
            if self.reinit_extinct:
                reinit_offspring += len(self.mod_species[spec_id])
            for mod_id in self.mod_species[spec_id]:
                del self.modules[mod_id]
            del self.mod_species[spec_id]
            del self.mod_species_repr[spec_id]
            del self.mod_species_fitness_history[spec_id]

        # If all species have been removed then abort and return positive population extinction flag
        if len(self.mod_species) == 0:
            return None, None, True

        print("FORCED EXIT")
        exit()

    def _select_modules_param_distance_dynamic(self) -> ({int: int}, int, bool):
        """"""
        # selection process identical for both variants of module speciation
        return self._select_modules_param_distance_fixed()
