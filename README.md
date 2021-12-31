# DataJoint Workflow-sensory-stimulation

Note: This README is still a work in progress.

A complete imaging workflow can be built using the DataJoint elements:
+ [element-lab](https://github.com/datajoint/element-lab)
+ [element-animal](https://github.com/datajoint/element-animal)
+ [element-session](https://github.com/datajoint/element-session)
+ [element-sensory-stimulation](https://github.com/datajoint/element-sensory-stimulation)

This repository provides demonstrations for:
1. Set up a workflow using different elements (see [workflow_sensory_stimulation/pipeline.py](workflow_sensory_stimulation/pipeline.py))
2. Ingestion of data/metadata based on:
    + predefined file/folder structure and naming convention
    + predefined directory lookup methods (see [workflow_sensory_stimulation/paths.py](workflow_sensory_stimulation/paths.py))
3. Ingestion of clustering results (built-in routine from the sensory-stimulation element)

## Workflow architecture

The Calcium imaging workflow presented here uses pipeline components from 4 DataJoint Elements, 
`element-lab`, `element-animal`, `element-session` and `element-sensory-stimulation`, assembled together to form a fully functional workflow. 

### element-lab

![element-lab](https://github.com/datajoint/element-lab/raw/main/images/element_lab_diagram.svg)

### element-animal

![element-animal](https://github.com/datajoint/element-animal/blob/main/images/subject_diagram.svg)

### assembled with element-sensory-stimulation


## Installation instructions

### Step 1 - Clone this repository

+ Launch a new terminal and change directory to where you want to clone the repository
    ```
    cd C:/Projects
    ```
+ Clone the repository
    ```
    git clone https://github.com/datajoint/workflow-sensory-stimulation
    ```
+ Change directory to `workflow-sensory-stimulation`
    ```
    cd workflow-sensory-stimulation
    ```

### Step 2 - Setup a virtual environment
+ It is highly recommended (though not strictly required) to create a virtual environment to run the pipeline.

+ You can install with `virtualenv` or `conda`.  Below are the commands for `virtualenv`.

+ If `virtualenv` not yet installed, run `pip install --user virtualenv`

+ To create a new virtual environment named `venv`:
    ```
    virtualenv venv
    ```

+ To activated the virtual environment:
    + On Windows:
        ```
        .\venv\Scripts\activate
        ```

    + On Linux/macOS:
        ```
        source venv/bin/activate
        ```

### Step 3 - Install this repository

From the root of the cloned repository directory:
    ```
    pip install -e .
    ```

Note: the `-e` flag will install this repository in editable mode, 
in case there's a need to modify the code (e.g. the `pipeline.py` or `paths.py` scripts). 
If no such modification required, using `pip install .` is sufficient

### Step 4 - Jupyter Notebook
+ Register an IPython kernel with Jupyter
    ```
    ipython kernel install --name=workflow-sensory-stimulation
    ```

### Step 5 - Configure the `dj_local_conf.json`

At the root of the repository folder, 
create a new file `dj_local_conf.json` with the following template:

```json
{
  "database.host": "<hostname>",
  "database.user": "<username>",
  "database.password": "<password>",
  "loglevel": "INFO",
  "safemode": true,
  "display.limit": 7,
  "display.width": 14,
  "display.show_tuple_count": true,
  "custom": {
      "database.prefix": "<neuro_>",
      "sensory_root_data_dir": "</data/sensory_root_data_dir>"
    }
}
```

+ Specify database's `hostname`, `username`, and `password` properly.

+ Specify a `database.prefix` to create the schemas.

+ Setup your data directory (`sensory_root_data_dir`) following the convention described below.

### Installation complete

+ At this point the setup of this workflow is complete.

## Directory structure and file naming convention

The workflow presented here is designed to work with the directory structure and file naming convention as described below.

Note: the `element-sensory-stimulation` is designed to accommodate multiple scans per session, 
however, in this particular `workflow-sensory-stimulation`, we take the assumption that there is only ***one scan per session***.

+ The `sensory_root_data_dir` directory is configurable in the `dj_local_conf.json`, under the `custom/sensory_root_data_dir` variable

+ The `subject` directory names must match the identifiers of your subjects in the [subjects.csv](./user_data/subjects.csv) script

+ The `session` directories can have any naming convention

## Running this workflow

See `notebooks/run_workflow.ipynb` for detailed instructions on running this workflow.

Once you have your data directory (`sensory_root_data_dir`) configured with the above convention, 
populating the workflow with your data amounts to these 3 steps:

1. Insert meta information (e.g. subject, sessions, equipment, Suite2p analysis parameters etc.) - modify:
    + user_data/subjects.csv
    + user_data/sessions.csv

2. Import session data - run:
    ```
    python workflow_sensory_stimulation/ingest.py
    ```

+ For inserting new subjects, sessions or new analysis parameters, step 1 needs to be repeated.

+ Rerun step 2 every time new sessions or processed data becomes available.

+ In fact, step 2 and 3 can be executed as scheduled jobs that will automatically process any data newly placed into the `sensory_root_data_dir`.

## Interacting with the DataJoint pipeline and exploring data

+ Connect to database and import tables
    ```
    from workflow_sensory_stimulation.pipeline import *
    ```

+ Query ingested data
    ```
    subject.Subject()
    session.Session()
    ```

+ If required to drop all schemas, the following is the dependency order. 
    ```
    from workflow_calcium_imaging.pipeline import *

    stimulation.schema.drop()
    session.schema.drop()
    subject.schema.drop()
    lab.schema.drop()
    ```

+ For a more in-depth exploration of ingested data, please refer to the example [notebook](notebooks/explore_workflow.ipynb).


## Developer Guide

### Development mode installation

This method allows you to modify the source code for `workflow-sensory-stimulation`, 
`element-sensory-stimulation`, `element-animal`, `element-session`, and `element-lab`.

+ Launch a new terminal and change directory to where you want to clone the repositories
    ```
    cd /Projects
    ```
+ Clone the repositories
    ```
    git clone https://github.com/datajoint/element-lab
    git clone https://github.com/datajoint/element-animal
    git clone https://github.com/datajoint/element-session
    git clone https://github.com/datajoint/element-sensory-stimulation
    git clone https://github.com/datajoint/workflow-sensory-stimulation
    ```
+ Install each package with the `-e` option
    ```
    pip install -e ./workflow-sensory-stimulation
    pip install -e ./element-session
    pip install -e ./element-lab
    pip install -e ./element-animal
    pip install -e ./element-sensory-stimulation
    ```
  
### Running tests

1. Download the test dataset to your local machine 
(note the directory where the dataset is saved at - e.g. `/tmp/testset`)

2. Create an `.env` file with the following content:

    > TEST_DATA_DIR=/tmp/testset
    
    (replace `/tmp/testset` with the directory where you have the test dataset downloaded to)
    
3. Run:

    
    docker-compose -f docker-compose-test.yaml up --build 
