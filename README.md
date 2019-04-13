[![Build Status](https://travis-ci.org/<github username>/<repo name>.svg?branch=master)](https://travis-ci.org/christopheralanjones/pypefitter)
[![Maintainability](https://api.codeclimate.com/v1/badges/46901ac1073649af704c/maintainability)](https://codeclimate.com/github/christopheralanjones/pypefitter/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/46901ac1073649af704c/test_coverage)](https://codeclimate.com/github/christopheralanjones/pypefitter/test_coverage)
# pypefitter
PypeFitter is a python-based software delivery pipeline generator. The goal is to allow for an abstract software delivery pipeline to be turned into concrete, executable implementations for providers like Jenkins or AWS.

An original implementation of this approach was provided for my employer, but that approach, while a servicable POC was comparatively rigid and the syntax for the pipeline definition felt clunky. In addition, I was unsuccessful in lobbying for that version to be made open source.

This new implementation is intended to address some of the shortcomings in the original form and to be open source so that contributions can be made from interested parties.

# Goals
Pypefitter's goals include:
* Provide an open-source tool that can be used to generate software delivery pipelines. Pipeline development is an industry-wide need, but while it is necessary, it is arguable if it is valuable. Our goal is to make it simple to get pipelines defined and implemented.
* Allow product teams to define their own pipelines without forcing them to learn about different concrete providers such as Jenkins or AWS.
* Enable the pipeline code to be versioned alongside the source code that it pipelines.
* Define a model by which complex integrations and lifecycles can be managed, but enable the pipeline authors to inject their own custom steps.
* Emphasize metadata and metrics. Pipelines are comparatively useful if we can't gain insights from them. Pypefitter endeavors to provide useful metrics and analytics right from the start.
 
