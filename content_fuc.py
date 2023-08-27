from utils import remove_after_string, to_package_format, to_snake_case, to_pascal_case, to_camel_case


def make_package(path, file_name):
    return remove_after_string(to_package_format(path), to_snake_case(file_name))


def fuc_content_case(path, file_name):
    packeage = make_package(path, file_name)
    file_name_pascal_case = to_pascal_case(file_name)
    conteudo = f"""
package {packeage};

import {packeage}.io.inputs.{file_name_pascal_case}UseCaseInput;
import {packeage}.io.outputs.{file_name_pascal_case}UseCaseOutput;
import {packeage}.specifics.functions.FunctionUseCase;

public abstract class {file_name_pascal_case}UseCase extends FunctionUseCase<{file_name_pascal_case}UseCaseInput, {file_name_pascal_case}UseCaseOutput> {{
    protected {file_name_pascal_case}UseCase() {{
        super();
    }}
}}
    """
    return conteudo



def fuc_content_factory(path, file_name):
    packeage = make_package(path, file_name)
    file_name_pascal_case = to_pascal_case(file_name)
    conteudo = f"""
package {packeage}.factories;

import {packeage}.CadastrarProdutoUseCase;
import {packeage}.factories.dependency_wrapper.CadastrarProdutoUseCaseDependencyWrapper;
import {packeage}.implementations.CadastrarProdutoUseCaseImplementation;
import lombok.AccessLevel;
import lombok.NoArgsConstructor;

import java.util.Optional;

@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class {file_name_pascal_case}UseCaseFactory {{

    private static {file_name_pascal_case}UseCase useCase = null;

    public static {file_name_pascal_case}UseCase generic({file_name_pascal_case}UseCaseDependencyWrapper dependencyWrapper){{
        if (Optional.ofNullable(useCase).isPresent())
            return useCase;
        useCase = makeInstanceWith(dependencyWrapper);
        return useCase;
    }}

    private static {file_name_pascal_case}UseCase makeInstanceWith({file_name_pascal_case}UseCaseDependencyWrapper dependencyWrapper) {{
        return new {file_name_pascal_case}UseCaseImplementation(
        );
    }}

}}"""
    return conteudo


def fuc_content_wrapper(path, file_name):
    packeage = make_package(path, file_name)
    file_name_pascal_case = to_pascal_case(file_name)
    file_name_camel_case = to_camel_case(file_name)

    conteudo = f"""
package {packeage}.factories.dependency_wrapper;

import br.com.stockio.use_cases.dependency_wrappers.UseCaseDependencyWrapper;
import {packeage}.implementations.ports.{file_name_pascal_case}Port;
import lombok.Builder;

@Builder
public class {file_name_pascal_case}UseCaseDependencyWrapper extends UseCaseDependencyWrapper {{

    private final {file_name_pascal_case}Port {file_name_camel_case}Port;
    private final {file_name_pascal_case}Factory {file_name_camel_case}Factory;

}}"""
    return conteudo