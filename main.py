from core.use_cases.java_web_use_case.ArchFlowJavaWeb import ArchFlowJavaWeb

arch = ArchFlowJavaWeb()


if __name__ == "__main__":
    args = ["teste", "vinicius"]
    arch.DirectoryCreator.create_folder("teste")
    arch.create_file_based_in_template("/teste/", "pom.txt", args)
    input()
    args = arch.handle_args()
    arch.handler_input(args)
