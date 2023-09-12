from utils import remove_after_string, to_package_format, to_snake_case, to_pascal_case, to_camel_case


def make_package(path, file_name):
    return remove_after_string(to_package_format(path), to_snake_case(file_name))


def fuc_content_case(path, file_name):
    packeage = make_package(path, file_name)
    packeage_not_use_case = remove_after_string(packeage, "use_cases")
    file_name_pascal_case = to_pascal_case(file_name)
    conteudo = f"""package {packeage};

import {packeage_not_use_case}.loggers.Logger;
import {packeage}.metadata.UseCaseMetadata;
import {packeage}.io.inputs.{file_name_pascal_case}UseCaseInput;
import {packeage}.io.outputs.{file_name_pascal_case}UseCaseOutput;
import {packeage}.specifics.functions.FunctionUseCase;

public abstract class {file_name_pascal_case}UseCase extends FunctionUseCase<{file_name_pascal_case}UseCaseInput, {file_name_pascal_case}UseCaseOutput> {{
    protected {file_name_pascal_case}UseCase(Logger logger) {{
        super(
                UseCaseMetadata.ofOpenAccessUseCase({file_name_pascal_case}UseCase.class, "some description about this use case"),
                logger
        );
    }}
}}
    """
    return conteudo


def fuc_content_factory(path, file_name):
    packeage = make_package(path, file_name)
    file_name_pascal_case = to_pascal_case(file_name)
    conteudo = f"""package {packeage}.factories;

import {packeage}.{file_name_pascal_case};
import {packeage}.factories.dependency_wrapper.{file_name_pascal_case}UseCaseDependencyWrapper;
import {packeage}.implementations.{file_name_pascal_case}UseCaseImplementation;

import java.util.Optional;

public class {file_name_pascal_case}UseCaseFactory {{

    private {file_name_pascal_case}UseCaseFactory(){{}}

    private static {file_name_pascal_case}UseCase singleton = null;

    public static {file_name_pascal_case}UseCase makeInstance({file_name_pascal_case}UseCaseDependencyWrapper dependencyWrapper){{
        return Optional.ofNullable(singleton).orelseGet(() -> {{
            singleton = new {file_name_pascal_case}UseCaseImplementation(dependencyWrapper.getLogger());
            return singleton;
        }});
    }}

    public static Optional<{file_name_pascal_case}> getSingleton() {{ return Optional.ofNullable(singleton);}}

}}"""
    return conteudo


def fuc_content_wrapper(path, file_name):
    packeage = make_package(path, file_name)
    file_name_pascal_case = to_pascal_case(file_name)
    packeage_not_use_case = remove_after_string(packeage, "use_cases")

    conteudo = f"""package {packeage}.factories.dependency_wrapper;

import {packeage_not_use_case}.Loggers.loggers;
import {packeage}.dependency_wrappers.UseCaseDependencyWrapper;

public class {file_name_pascal_case}UseCaseDependencyWrapper extends UseCaseDependencyWrapper {{

    //declare here the dependencies your uses case has
    private final Logger logger;

    public {file_name_pascal_case}UseCaseDependencyWrapper(Logger logger) {{this.logger = logger;}}

    //it is a good thing to make sure the attributes aren´t null, unless explicitly intended otherwise

    public Logger getLogger() {{return this.getValueWithNullSafety(this.logger);}}

    }}
"""
    return conteudo


def fuc_content_implementations(path, file_name):
    packeage = make_package(path, file_name)
    packeage_not_use_case = remove_after_string(packeage, "use_cases")
    file_name_pascal_case = to_pascal_case(file_name)
    conteudo = f"""package {packeage}.implementations;

import {packeage_not_use_case}.loggers.Logger;
import {packeage_not_use_case}.use_cases.correlations.UseCaseExecutionCorrelation;
import {packeage}.{file_name_pascal_case}UseCase;
import {packeage}.io.inputs.{file_name_pascal_case}UseCaseInput;
import {packeage}.io.outputs.{file_name_pascal_case}UseCaseOutput;

public class {file_name_pascal_case}UseCaseImplementation extends {file_name_pascal_case}UseCase{{

    //declare here the ports and other dependencies you might need within this use case implementation

    public {file_name_pascal_case}UseCaseImplementation(Logger logger) {{super(logger);}}

    @Override
    protected {file_name_pascal_case}UseCaseOutput applyInternalLogic({file_name_pascal_case}UseCaseInput input, UseCaseExecutionCorrelation correlation) {{
    //implement the logic of the use case here. to make contact with dependencies from here, create ports.
    return null;
    }}
}}
    """
    return conteudo


def fuc_content_case_inputs(path, file_name):
    packeage = make_package(path, file_name)
    packeage_not_use_case = remove_after_string(packeage, "use_cases")
    file_name_pascal_case = to_pascal_case(file_name)
    conteudo = f"""package {packeage}.io.inputs;

import {packeage}.io.UseCaseInput;

public class {file_name_pascal_case}UseCaseInput extends UseCaseInput {{
    //Define the attributes for the input of the {file_name_pascal_case}UseCase here.
}}
    """
    return conteudo


def fuc_content_case_outputs(path, file_name):
    packeage = make_package(path, file_name)
    packeage_not_use_case = remove_after_string(packeage, "use_cases")
    file_name_pascal_case = to_pascal_case(file_name)
    conteudo = f"""package {packeage}.io.outputs;

import {packeage}.io.UseCaseInput;

public class {file_name_pascal_case}UseCaseOutput {{
    //Define the attributes for the output of the {file_name_pascal_case}UseCase here.
}}
    """
    return conteudo