# ceske-svatky
Tento jednoduchý program zobrazí po spuštění počítače oznámení o tom, kdo má dneska svátek. Funguje pouze online, protože k fungování využívá Svátky API (https://svatky.adresa.info/).

![svatky](https://user-images.githubusercontent.com/70912486/162619952-6f80d1ba-14b6-48b5-99fa-a7c0689205fd.gif)

## Instalace

Pro jednoduchou instalaci:
1. Přejděte do části Releases (https://github.com/Nextross/ceske-svatky/releases) a vyberte nejnovější verzi
2. Přetáhněte stažený soubor do složky `%USERNNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

Pro vytvoření vlastního `main.exe` souboru budete potřebovat pár věcí:
1. Nainstalovaný Python (https://www.python.org/downloads/)
2. Stažený zdrojový kód
3. Vytvořené virtuální prostředí (ve složce se zdrojovým kódem)
4. Nainstalované knihovny ve virtuálním prostředí `auto-py-to-exe` a `notify-py`

Pokud máte všechny tyto věci správně nainstalované, můžeme přejít na vytvoření `main.exe` souboru:
1. Do konzole se spuštěným virtuálním prostředím napište `auto-py-to-exe` (měl by se otevřít webový prohlížeč)
2. Do okna Script Location zadejte cestu k `main.py`
3. Zvolte One File, Window Based (hide the console)
4. Jako ikonu zvolte `icon.ico`
5. Do Additional Files (Add Files) přidejte `icon.ico`
6. V Advanced najděte `--hidden-import` - přidejte knihovnu `notify-py`
7. Klikněte na CONVERT .PY TO .EXE

## Lincence

Tento program se řídí podle GNU General Public License v3.0 licence.
