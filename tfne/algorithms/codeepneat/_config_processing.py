from ...helper_functions import read_option_from_config


class ConfigProcessing:
    def _process_config(self, config):
        """"""
        # Read and process the general config values for CoDeepNEAT
        self.dtype = read_option_from_config(config, 'GENERAL', 'dtype')
        self.bp_pop_size = read_option_from_config(config, 'GENERAL', 'bp_pop_size')
        self.mod_pop_size = read_option_from_config(config, 'GENERAL', 'mod_pop_size')
        self.genomes_per_bp = read_option_from_config(config, 'GENERAL', 'genomes_per_bp')
        self.eval_epochs = read_option_from_config(config, 'GENERAL', 'eval_epochs')
        self.eval_batch_size = read_option_from_config(config, 'GENERAL', 'eval_batch_size')

        # Read and process the config values that concern the genome creation for CoDeepNEAT
        self.available_modules = read_option_from_config(config, 'GENOME', 'available_modules')
        self.available_optimizers = read_option_from_config(config, 'GENOME', 'available_optimizers')
        self.preprocessing = read_option_from_config(config, 'GENOME', 'preprocessing')
        self.output_layers = read_option_from_config(config, 'GENOME', 'output_layers')

        # Adjust output_layers config to include the configured datatype
        for out_layer in self.output_layers:
            out_layer['config']['dtype'] = self.dtype

        # Read and process the config values that concern the module speciation for CoDeepNEAT
        self.mod_spec_type = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_type')
        if self.mod_spec_type == 'basic':
            self.mod_spec_mod_elitism = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_mod_elitism')
            self.mod_spec_min_offspring = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_min_offspring')
            self.mod_spec_reprod_thres = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_reprod_thres')
        elif self.mod_spec_type == 'param-distance-fixed':
            self.mod_spec_distance = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_distance')
            self.mod_spec_mod_elitism = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_mod_elitism')
            self.mod_spec_min_offspring = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_min_offspring')
            self.mod_spec_reprod_thres = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_reprod_thres')
            self.mod_spec_max_stagnation = read_option_from_config(config,
                                                                   'MODULE_SPECIATION',
                                                                   'mod_spec_max_stagnation')
            self.mod_spec_species_elitism = read_option_from_config(config,
                                                                    'MODULE_SPECIATION',
                                                                    'mod_spec_species_elitism')
            self.mod_spec_rebase_repr = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_rebase_repr')
            self.mod_spec_reinit_extinct = read_option_from_config(config,
                                                                   'MODULE_SPECIATION',
                                                                   'mod_spec_reinit_extinct')
        elif self.mod_spec_type == 'param-distance-dynamic':
            self.mod_spec_species_count = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_species_count')
            self.mod_spec_distance = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_distance')
            self.mod_spec_mod_elitism = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_mod_elitism')
            self.mod_spec_min_offspring = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_min_offspring')
            self.mod_spec_reprod_thres = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_reprod_thres')
            self.mod_spec_max_stagnation = read_option_from_config(config,
                                                                   'MODULE_SPECIATION',
                                                                   'mod_spec_max_stagnation')
            self.mod_spec_species_elitism = read_option_from_config(config,
                                                                    'MODULE_SPECIATION',
                                                                    'mod_spec_species_elitism')
            self.mod_spec_rebase_repr = read_option_from_config(config, 'MODULE_SPECIATION', 'mod_spec_rebase_repr')
            self.mod_spec_reinit_extinct = read_option_from_config(config,
                                                                   'MODULE_SPECIATION',
                                                                   'mod_spec_reinit_extinct')
        else:
            raise NotImplementedError(f"Module speciation type '{self.mod_spec_type}' not yet implemented")

        # Read and process the config values that concern the evolution of modules for CoDeepNEAT
        self.mod_max_mutation = read_option_from_config(config, 'MODULE_EVOLUTION', 'mod_max_mutation')
        self.mod_mutation_prob = read_option_from_config(config, 'MODULE_EVOLUTION', 'mod_mutation_prob')
        self.mod_crossover_prob = read_option_from_config(config, 'MODULE_EVOLUTION', 'mod_crossover_prob')

        # Read and process the config values that concern the blueprint speciation for CoDeepNEAT
        self.bp_spec_type = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_type')
        if self.bp_spec_type == 'basic':
            self.bp_spec_bp_elitism = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_bp_elitism')
            self.bp_spec_reprod_thres = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_reprod_thres')
        elif self.bp_spec_type == 'gene-overlap-fixed':
            self.bp_spec_distance = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_distance')
            self.bp_spec_bp_elitism = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_bp_elitism')
            self.bp_spec_min_offspring = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_min_offspring')
            self.bp_spec_reprod_thres = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_reprod_thres')
            self.bp_spec_max_stagnation = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_max_stagnation')
            self.bp_spec_species_elitism = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_species_elitism')
            self.bp_spec_rebase_repr = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_rebase_repr')
            self.bp_spec_reinit_extinct = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_reinit_extinct')
        elif self.bp_spec_type == 'gene-overlap-dynamic':
            self.bp_spec_species_count = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_species_count')
            self.bp_spec_distance = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_distance')
            self.bp_spec_bp_elitism = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_bp_elitism')
            self.bp_spec_min_offspring = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_min_offspring')
            self.bp_spec_reprod_thres = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_reprod_thres')
            self.bp_spec_max_stagnation = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_max_stagnation')
            self.bp_spec_species_elitism = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_species_elitism')
            self.bp_spec_rebase_repr = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_rebase_repr')
            self.bp_spec_reinit_extinct = read_option_from_config(config, 'BP_SPECIATION', 'bp_spec_reinit_extinct')
        else:
            raise NotImplementedError(f"Blueprint speciation type '{self.bp_spec_type}' not yet implemented")

        # Read and process the config values that concern the evolution of blueprints for CoDeepNEAT
        self.bp_max_mutation = read_option_from_config(config, 'BP_EVOLUTION', 'bp_max_mutation')
        self.bp_mutation_add_conn_prob = read_option_from_config(config, 'BP_EVOLUTION', 'bp_mutation_add_conn_prob')
        self.bp_mutation_add_node_prob = read_option_from_config(config, 'BP_EVOLUTION', 'bp_mutation_add_node_prob')
        self.bp_mutation_rem_conn_prob = read_option_from_config(config, 'BP_EVOLUTION', 'bp_mutation_rem_conn_prob')
        self.bp_mutation_rem_node_prob = read_option_from_config(config, 'BP_EVOLUTION', 'bp_mutation_rem_node_prob')
        self.bp_mutation_node_spec_prob = read_option_from_config(config, 'BP_EVOLUTION', 'bp_mutation_node_spec_prob')
        self.bp_mutation_optimizer_prob = read_option_from_config(config, 'BP_EVOLUTION', 'bp_mutation_optimizer_prob')
        self.bp_crossover_prob = read_option_from_config(config, 'BP_EVOLUTION', 'bp_crossover_prob')

        # Read and process the config values that concern the parameter range of the modules for CoDeepNEAT
        self.available_mod_params = dict()
        for available_mod in self.available_modules:
            # Determine a dict of all supplied configuration values as literal evals
            config_section_str = 'MODULE_' + available_mod.upper()
            if not config.has_section(config_section_str):
                raise RuntimeError(f"Module '{available_mod}' marked as available in config does not have an "
                                   f"associated config section defining its parameters")
            mod_section_params = dict()
            for mod_param in config.options(config_section_str):
                mod_section_params[mod_param] = read_option_from_config(config, config_section_str, mod_param)

            # Assign that dict of all available parameters for the module to the instance variable
            self.available_mod_params[available_mod] = mod_section_params

        # Read and process the config values that concern the parameter range of the optimizers for CoDeepNEAT
        self.available_opt_params = dict()
        for available_opt in self.available_optimizers:
            # Determine a dict of all supplied configuration values as literal evals
            config_section_str = 'OPTIMIZER_' + available_opt.upper()
            if not config.has_section(config_section_str):
                raise RuntimeError(f"Optimizer '{available_opt}' marked as available in config does not have an "
                                   f"associated config section defining its parameters")
            opt_section_params = dict()
            for opt_param in config.options(config_section_str):
                opt_section_params[opt_param] = read_option_from_config(config, config_section_str, opt_param)

            # Assign that dict of all available parameters for the optimizers to the instance variable
            self.available_opt_params[available_opt] = opt_section_params

        # Perform some basic sanity checks of the configuration
        assert round(self.mod_mutation_prob + self.mod_crossover_prob, 4) == 1.0
        assert round(self.bp_mutation_add_conn_prob + self.bp_mutation_add_node_prob + self.bp_mutation_rem_conn_prob
                     + self.bp_mutation_rem_node_prob + self.bp_mutation_node_spec_prob + self.bp_crossover_prob
                     + self.bp_mutation_optimizer_prob, 4) == 1.0
