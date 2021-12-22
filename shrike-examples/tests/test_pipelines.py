"""
PyTest suite for testing all runnable pipelines.
"""

import sys
from unittest.mock import patch

# import pipeline class
#from pipelines.experiments.demo_subgraph import DemoGraphWithSubgraph
from pipelines.experiments.demo_dynamic_graph import DynamicGraphDemo

### Pipeline validation tests (integration tests)

def test_demo_subgraph_build_local(pipeline_config_path="pipelines/config"):
    """ Tests the subgraph demo graph by running the main function itself (which does .validate()) """
    testargs = [
        "prog",
        "--config-dir",
        pipeline_config_path,
        "--config-name",
        # "experiments/demo_subgraph", # To-Do: point to the right config file
        "experiments/demo_dynamic_graph",
        "module_loader.use_local='*'", # To-Do: make sure the local version is used for ALL components - '*' could be helpful here
    ]
    # will do everything except submit :)
    with patch.object(sys, "argv", testargs):
        #DemoGraphWithSubgraph.main()
        DynamicGraphDemo.main()
        # To-Do: call the main method of your pipeline
