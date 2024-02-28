from core.use_cases.java_web_use_case.ArchFlowJavaWeb import ArchFlowJavaWeb

arch = ArchFlowJavaWeb()


if __name__ == "__main__":
    print(arch.read_file_template("templates/pom.txt"))
    input()
    args = arch.handle_args()
    arch.handler_input(args)
