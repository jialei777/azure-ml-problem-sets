"""
The AML subgraph for demo graph
"""
# pylint: disable=no-member
# NOTE: because it raises 'dict' has no 'outputs' member in dsl.pipeline construction
import os
import sys
from dataclasses import dataclass
from typing import Optional

from azure.ml.component import dsl
from shrike.pipeline.pipeline_helper import AMLPipelineHelper

# NOTE: if you need to import from pipelines.*
ACCELERATOR_ROOT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if ACCELERATOR_ROOT_PATH not in sys.path:
    print(f"Adding to path: {ACCELERATOR_ROOT_PATH}")
    sys.path.append(str(ACCELERATOR_ROOT_PATH))


class DemoSubgraph(AMLPipelineHelper): # rename the class as DemoSubgraph
    """Runnable/reusable pipeline helper class

    This class inherits from AMLPipelineHelper which provides
    helper functions to create reusable production pipelines.
    """

    def build(self, config):
        """Builds a pipeline function for this pipeline using AzureML SDK (dsl.pipeline).

        This method should build your graph using the provided config object.
        Your pipeline config will be under config.CONFIGNAME.*
        where CONFIGNAME is the name of the dataclass returned by get_config_class()

        This method returns a constructed pipeline function (decorated with @dsl.pipeline).

        Args:
            config (DictConfig): configuration object (see get_config_class())

        Returns:
            dsl.pipeline: the function to create your pipeline
        """

        # helper function below loads the module from registered or local version depending on your config run.use_local
        probe_component = self.component_load("probe")

        # Here you should create an instance of a pipeline function (using your custom config dataclass)
        @dsl.pipeline(
            name="demo-subgraph",
            description="The AML pipeline for the demo subgraph",
            default_datastore=config.compute.compliant_datastore,
        )
        def demosubgraph_pipeline_function( # rename it to demosubgraph_pipeline_function 
            probe_dataset,
            param_scan_args=True,  # add all those input values
            param_scan_deps=True, 
            param_scan_input=True, 
            param_scan_env_1=True, 
            param_scan_env_2=False,
            param_verbose=True, 
        ):
            """Pipeline function for this graph.

            Args:
                inputdataset (FileDataset) : the input eyes-on/eyes-off dataset provided as parquet files

            Returns:
                dict[str->PipelineOutputData]: a dictionary of your pipeline outputs
                    for instance to be consumed by other graphs
            """
            # general syntax:
            # module_instance = module_class(input=data, param=value)
            # or
            # subgraph_instance = subgraph_function(input=data, param=value)
            probe_component_step_1 = probe_component(
                input_data=probe_dataset,
                scan_args=param_scan_args,
                scan_deps=param_scan_deps, 
                scan_input=param_scan_input, 
                scan_env=param_scan_env_1, 
                verbose=param_verbose,
            )

            self.apply_recommended_runsettings(
                "probe", probe_component_step_1, gpu=True
            )

            probe_component_step_2 = probe_component(
                input_data=probe_component_step_1.outputs.results,  # this is where we pipe the output of the first module to the input of the second module
                scan_args=param_scan_args,
                scan_deps=param_scan_deps, 
                scan_input=param_scan_input, 
                scan_env=param_scan_env_2, 
                verbose=param_verbose,
            )

            self.apply_recommended_runsettings(
                "probe", probe_component_step_2, gpu=True
            )

            # return {key: output}
            return {"subgraph_results": probe_component_step_2.outputs.results}

        # finally return the function itself to be built by helper code
        return demosubgraph_pipeline_function
