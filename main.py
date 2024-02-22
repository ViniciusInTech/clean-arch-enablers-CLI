from core.use_cases.java_web_use_case.ArchFlowJavaWeb import ArchFlowJavaWeb

arch = ArchFlowJavaWeb()


if __name__ == "__main__":
    args = arch.handle_args()
    arch.handler_input(args)
