@echo off

:: Find the first subdirectory in the download path
for /d %%D in ("%~1\*") do (
    set "REPO_DIR=%%D"
)

if not defined REPO_DIR (
    echo ERROR: No repository directory found.
    pause
    exit /b 1
)

:: Verifica se o diretório %USERPROFILE%\cae existe
if exist %USERPROFILE%\cae (
    echo Found the cae directory. Using it.
) else (
    echo Not found cae directory. Creating it.
    mkdir %USERPROFILE%\cae
)

:: Cria o arquivo cae.bat no diretório %USERPROFILE%\cae
echo @echo off > %USERPROFILE%\cae\cae.bat
echo java -jar %USERPROFILE%\cae\cae-cli.jar %%* >> %USERPROFILE%\cae\cae.bat

:: Configura variáveis de ambiente
setx CAE_CLI_HOME "%USERPROFILE%\cae"
setx CAE_META_STRUCTURE_TEMPLATES_PATH "%USERPROFILE%\cae\file-templates"

:: Atualiza o arquivo .bashrc, se existir
if exist %USERPROFILE%\.bashrc (
    echo alias cae='cmd //c cae' >> %USERPROFILE%\.bashrc
    echo export CAE_META_STRUCTURE_TEMPLATES_PATH="${CAE_META_STRUCTURE_TEMPLATES_PATH}" >> %USERPROFILE%\.bashrc
) else (
    echo .bashrc não encontrado. Pulando atualização de alias.
)

:: Find cae-cli.jar in the repository directory
for /r "%REPO_DIR%" %%F in (cae-cli.jar) do (
    set "JAR_PATH=%%F"
)

if defined JAR_PATH (
    copy "%JAR_PATH%" %USERPROFILE%\cae
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao copiar cae-cli.jar. Verifique permissões ou caminho.
        pause
        exit /b 1
    )
) else (
    echo ERRO: O arquivo cae-cli.jar não foi encontrado no diretório do repositório.
    pause
    exit /b 1
)

:: Find file-templates directory
for /d /r "%REPO_DIR%" %%D in (file-templates) do (
    set "TEMPLATES_DIR=%%D"
)

if defined TEMPLATES_DIR (
    xcopy "%TEMPLATES_DIR%" %USERPROFILE%\cae\file-templates /E /I /H /Y
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao copiar os arquivos do diretório file-templates.
        pause
        exit /b 1
    )
) else (
    echo ERRO: O diretório file-templates não foi encontrado no repositório.
    pause
    exit /b 1
)

:: Mensagem final e pausa
echo Configuração concluída com sucesso!
pause