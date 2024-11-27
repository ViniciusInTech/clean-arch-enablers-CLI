::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFBFbXwGOAEi7FrwI5+Ty4Nakg2ghV+M6NYzX04iHLvMH60nocIQR1Xtf1cgABVZRcAG/bwM4rHwMs3yAVw==
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983

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

:: Verifica se o arquivo cae-cli.jar existe no caminho esperado e copia para o diretório %USERPROFILE%\cae
if exist .\components\cae-cli.jar (
    copy .\components\cae-cli.jar %USERPROFILE%\cae
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao copiar cae-cli.jar. Verifique permissões ou caminho.
        pause
        exit /b
    )
) else (
    echo ERRO: O arquivo cae-cli.jar não foi encontrado no diretório .\components.
    pause
    exit /b
)

:: Verifica se o diretório file-templates existe e copia para %USERPROFILE%\cae\file-templates
if exist .\components\file-templates (
    xcopy .\components\file-templates %USERPROFILE%\cae\file-templates /E /I /H /Y
    if %errorlevel% neq 0 (
        echo ERRO: Falha ao copiar os arquivos do diretório file-templates.
        pause
        exit /b
    )
) else (
    echo ERRO: O diretório file-templates não foi encontrado em .\components.
    pause
    exit /b
)

:: Mensagem final e pausa
echo Configuração concluída com sucesso!
pause