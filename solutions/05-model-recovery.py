import cpm
import warnings
from packaging import version


if __name__ == "__main__":
    import numpy
    import pandas as pd
    import cpm
    import cpm.datasets as datasets
    import functions as f
    
    data = datasets.load_bandit_data()
    data["observed"] = data["response"].astype(int)  # convert responses to int
    data.head()

    ## we create all the difference models we want to compare
    model_one_generative, model_one_fitting, parameters = f.model_delta(data)
    model_two_generative, model_two_fitting, parameters_two = f.model_kernel(data)
    model_three_generative, model_three_fitting, parameters_three = f.model_anticorrelated(data)

    ## we create a list of the generative models, parameters and fitting methods
    # to make it easier to loop through them later
    generators = (
        model_one_generative,
        model_two_generative,
        model_three_generative,
    )

    parameter_sets = (
        parameters,
        parameters_two,
        parameters_three,
    )

    fitting = (
        model_one_fitting,
        model_two_fitting,
        model_three_fitting,
    )

    ## we create a list of the model names to use later for plots and data organisation
    ## this is just for convenience, you can use any names you like
    model_names = (
        "delta",
        "kernel",
        "anticorrelated"
    )

    ## we create a copy of the data to use for the simulations
    ## this is to ensure that we do not modify the original data
    ## and to keep the data structure consistent
    dataset = data.copy()

    ## we run the simulations and fitting for each model
    bigout = pd.DataFrame()
    for x in numpy.arange(100):
        print(f"Run {x + 1} of 100")
        for i in numpy.arange(3):
            ## we create a simulator for each model
            ## the simulator will generate data based on the model and parameters
            ## for many participants
            simulator = cpm.generators.Simulator(
                wrapper=generators[i],
                parameters=parameter_sets[i].sample(dataset.ppt.nunique()),
                data=data.groupby("ppt")
            )
            simulator.run()
            out = simulator.export()
            ## we add the simulated data to the dataset
            ## essentially overwriting the observed variable with
            ## the simulated responses
            dataset["observed"] = out.response_0
            ## now we fit all models to the simualted data
            for m in numpy.arange(3):
                model = fitting[m]
                ## mute runtime warings
                warnings.filterwarnings("ignore", category=RuntimeWarning)
                fit = cpm.optimisation.FminBound(
                    model=model,  # Wrapper class with the model we specified from before
                    data=dataset.groupby('ppt'),  # the data as a list of dictionaries
                    minimisation=cpm.optimisation.minimise.LogLikelihood.bernoulli,
                    parallel=True,
                    prior=False,
                    ppt_identifier="ppt",
                    display=False,
                    number_of_starts=5,
                    # everything below is optional and passed directly to the scipy implementation of the optimiser
                    approx_grad=True
                )
                fit.optimise()
                output = fit.export()
                output["target"] = model_names[i]
                output["model"] = model_names[m]
                output["run"] = x
                bigout = pd.concat([bigout, output], ignore_index=True)

    bigout.to_csv("./solutions/05-model-recovery-results.csv", index=False)
