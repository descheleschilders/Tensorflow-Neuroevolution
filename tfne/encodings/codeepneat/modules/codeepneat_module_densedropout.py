from __future__ import annotations

import math
import random
import statistics

import numpy as np
import tensorflow as tf

from .codeepneat_module_base import CoDeepNEATModuleBase
from ....helper_functions import round_with_step


class CoDeepNEATModuleDenseDropout(CoDeepNEATModuleBase):
    """"""

    def __init__(self,
                 config_params,
                 module_id,
                 parent_mutation,
                 dtype,
                 merge_method=None,
                 units=None,
                 activation=None,
                 kernel_init=None,
                 bias_init=None,
                 dropout_flag=None,
                 dropout_rate=None,
                 self_initialization_flag=False):
        """"""
        # Register the implementation specifics by calling parent class
        super().__init__(config_params, module_id, parent_mutation, dtype)

        # Register the module parameters
        self.merge_method = merge_method
        self.units = units
        self.activation = activation
        self.kernel_init = kernel_init
        self.bias_init = bias_init
        self.dropout_flag = dropout_flag
        self.dropout_rate = dropout_rate

        # If self initialization flag is provided, initialize the module parameters as they are currently set to None
        if self_initialization_flag:
            self.initialize()

    def __str__(self) -> str:
        """"""
        return "CoDeepNEAT DENSE Module | ID: {:>6} | Fitness: {:>6} | Units: {:>4} | Activ: {:>6} | Dropout: {:>4}" \
            .format('#' + str(self.module_id),
                    self.fitness,
                    self.units,
                    self.activation,
                    "None" if self.dropout_flag is False else self.dropout_rate)

    def initialize(self):
        """"""
        # Uniformly randomly set module parameters
        self.merge_method = random.choice(self.config_params['merge_method'])
        random_units = random.randint(self.config_params['units']['min'],
                                      self.config_params['units']['max'])
        self.units = round_with_step(random_units,
                                     self.config_params['units']['min'],
                                     self.config_params['units']['max'],
                                     self.config_params['units']['step'])
        self.activation = random.choice(self.config_params['activation'])
        self.kernel_init = random.choice(self.config_params['kernel_init'])
        self.bias_init = random.choice(self.config_params['bias_init'])
        self.dropout_flag = random.random() < self.config_params['dropout_flag']
        random_dropout_rate = random.uniform(self.config_params['dropout_rate']['min'],
                                             self.config_params['dropout_rate']['max'])
        self.dropout_rate = round(round_with_step(random_dropout_rate,
                                                  self.config_params['dropout_rate']['min'],
                                                  self.config_params['dropout_rate']['max'],
                                                  self.config_params['dropout_rate']['step']), 4)

    def create_mutation(self,
                        offspring_id,
                        max_degree_of_mutation) -> CoDeepNEATModuleDenseDropout:
        """"""
        # Copy the parameters of this parent module for the parameters of the offspring
        offspring_params = {'merge_method': self.merge_method,
                            'units': self.units,
                            'activation': self.activation,
                            'kernel_init': self.kernel_init,
                            'bias_init': self.bias_init,
                            'dropout_flag': self.dropout_flag,
                            'dropout_rate': self.dropout_rate}

        # Create the dict that keeps track of the mutations occuring for the offspring
        parent_mutation = {'parent_id': self.module_id,
                           'mutation': 'mutation',
                           'mutated_params': dict()}

        # Determine exact integer amount of parameters to be mutated, though minimum is 1
        param_mutation_count = math.ceil(max_degree_of_mutation * 7)

        # Uniform randomly choose the parameters to be mutated
        parameters_to_mutate = random.sample(range(7), k=param_mutation_count)

        # Mutate offspring parameters. Categorical parameters are chosen randomly from all available values. Sortable
        # parameters are perturbed through a random normal distribution with the current value as mean and the config
        # specified stddev
        for param_to_mutate in parameters_to_mutate:
            if param_to_mutate == 0:
                offspring_params['merge_method'] = random.choice(self.config_params['merge_method'])
                parent_mutation['mutated_params']['merge_method'] = self.merge_method
            elif param_to_mutate == 1:
                perturbed_units = int(np.random.normal(loc=self.units,
                                                       scale=self.config_params['units']['stddev']))
                offspring_params['units'] = round_with_step(perturbed_units,
                                                            self.config_params['units']['min'],
                                                            self.config_params['units']['max'],
                                                            self.config_params['units']['step'])
                parent_mutation['mutated_params']['units'] = self.units
            elif param_to_mutate == 2:
                offspring_params['activation'] = random.choice(self.config_params['activation'])
                parent_mutation['mutated_params']['activation'] = self.activation
            elif param_to_mutate == 3:
                offspring_params['kernel_init'] = random.choice(self.config_params['kernel_init'])
                parent_mutation['mutated_params']['kernel_init'] = self.kernel_init
            elif param_to_mutate == 4:
                offspring_params['bias_init'] = random.choice(self.config_params['bias_init'])
                parent_mutation['mutated_params']['bias_init'] = self.bias_init
            elif param_to_mutate == 5:
                offspring_params['dropout_flag'] = not self.dropout_flag
                parent_mutation['mutated_params']['dropout_flag'] = self.dropout_flag
            else:  # param_to_mutate == 6:
                perturbed_dropout_rate = np.random.normal(loc=self.dropout_rate,
                                                          scale=self.config_params['dropout_rate']['stddev'])
                offspring_params['dropout_rate'] = round(round_with_step(perturbed_dropout_rate,
                                                                         self.config_params['dropout_rate']['min'],
                                                                         self.config_params['dropout_rate']['max'],
                                                                         self.config_params['dropout_rate']['step']), 4)
                parent_mutation['mutated_params']['dropout_rate'] = self.dropout_rate

        return CoDeepNEATModuleDenseDropout(config_params=self.config_params,
                                            module_id=offspring_id,
                                            parent_mutation=parent_mutation,
                                            dtype=self.dtype,
                                            **offspring_params)

    def create_crossover(self,
                         offspring_id,
                         less_fit_module,
                         max_degree_of_mutation) -> CoDeepNEATModuleDenseDropout:
        """"""
        # Create offspring parameters by carrying over parameters of fitter parent for categorical parameters and
        # calculating parameter average between both modules for sortable parameters
        offspring_params = dict()

        # Create the dict that keeps track of the mutations occuring for the offspring
        parent_mutation = {'parent_id': (self.module_id, less_fit_module.get_id()),
                           'mutation': 'crossover'}

        offspring_params['merge_method'] = self.merge_method
        offspring_params['units'] = round_with_step(int((self.units + less_fit_module.units) / 2),
                                                    self.config_params['units']['min'],
                                                    self.config_params['units']['max'],
                                                    self.config_params['units']['step'])
        offspring_params['activation'] = self.activation
        offspring_params['kernel_init'] = self.kernel_init
        offspring_params['bias_init'] = self.bias_init
        offspring_params['dropout_flag'] = self.dropout_flag
        offspring_params['dropout_rate'] = round(round_with_step((self.dropout_rate + less_fit_module.dropout_rate) / 2,
                                                                 self.config_params['dropout_rate']['min'],
                                                                 self.config_params['dropout_rate']['max'],
                                                                 self.config_params['dropout_rate']['step'], ), 4)

        return CoDeepNEATModuleDenseDropout(config_params=self.config_params,
                                            module_id=offspring_id,
                                            parent_mutation=parent_mutation,
                                            dtype=self.dtype,
                                            **offspring_params)

    def create_module_layers(self) -> [tf.keras.layers.Layer, ...]:
        """"""
        # Create the basic keras Dense layer, needed in all variants of the module
        dense_layer = tf.keras.layers.Dense(units=self.units,
                                            activation=self.activation,
                                            kernel_initializer=self.kernel_init,
                                            bias_initializer=self.bias_init,
                                            dtype=self.dtype)

        # If no dropout flag present, return solely the created dense layer as iterable. If dropout flag present, return
        # the dense layer and together with the dropout layer
        if not self.dropout_flag:
            return (dense_layer,)
        else:
            dropout_layer = tf.keras.layers.Dropout(rate=self.dropout_rate,
                                                    dtype=self.dtype)
            return dense_layer, dropout_layer

    def create_downsampling_layer(self, in_shape, out_shape) -> tf.keras.layers.Layer:
        """"""
        raise NotImplementedError("Downsampling has not yet been implemented for DenseDropout Modules")

    def serialize(self) -> dict:
        """"""
        return {
            'module_type': self.get_module_type(),
            'module_id': self.module_id,
            'parent_mutation': self.parent_mutation,
            'merge_method': self.merge_method,
            'units': self.units,
            'activation': self.activation,
            'kernel_init': self.kernel_init,
            'bias_init': self.bias_init,
            'dropout_flag': self.dropout_flag,
            'dropout_rate': self.dropout_rate
        }

    def get_distance(self, other_module) -> float:
        """"""
        # Calculate distance of modules by inspecting each parameter, calculating the congruence between each and
        # eventually averaging the out the congruence. The distance is returned as the average congruences distance to
        # 1.0. The congruence of continuous parameters is calculated by their relative distance. The congruence of
        # categorical parameters is either 1.0 in case they are the same or it's 1 divided to the amount of possible
        # values for that specific parameter
        congruence_list = list()
        if self.merge_method == other_module.merge_method:
            congruence_list.append(1.0)
        else:
            congruence_list.append(1 / len(self.config_params['merge_method']))
        if self.units >= other_module.units:
            congruence_list.append(other_module.units / self.units)
        else:
            congruence_list.append(self.units / other_module.units)
        if self.activation == other_module.activation:
            congruence_list.append(1.0)
        else:
            congruence_list.append(1 / len(self.config_params['activation']))
        if self.kernel_init == other_module.kernel_init:
            congruence_list.append(1.0)
        else:
            congruence_list.append(1 / len(self.config_params['kernel_init']))
        if self.bias_init == other_module.bias_init:
            congruence_list.append(1.0)
        else:
            congruence_list.append(1 / len(self.config_params['bias_init']))
        congruence_list.append(abs(self.dropout_flag - other_module.dropout_flag))
        if self.dropout_rate >= other_module.dropout_rate:
            congruence_list.append(other_module.dropout_rate / self.dropout_rate)
        else:
            congruence_list.append(self.dropout_rate / other_module.dropout_rate)

        # Return the distance as the distance of the average congruence to the perfect congruence of 1.0
        return 1.0 - statistics.mean(congruence_list)

    def get_module_type(self) -> str:
        """"""
        return 'DenseDropout'
