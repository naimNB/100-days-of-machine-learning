# Ubuntu GNOME Top Taskbar Setup

This note keeps the working commands used to make Ubuntu GNOME look like a thin top taskbar/panel using Dash to Panel.

## Install Dash to Panel from source

```bash
sudo apt install git make gettext -y

cd ~
rm -rf dash-to-panel
git clone https://github.com/home-sweet-gnome/dash-to-panel.git
cd dash-to-panel
make install
```

After installation, log out and log back in.

## Fix the GSettings schema if needed

If you see:

```text
No such schema “org.gnome.shell.extensions.dash-to-panel”
```

run:

```bash
mkdir -p ~/.local/share/glib-2.0/schemas

cp ~/.local/share/gnome-shell/extensions/dash-to-panel@jderose9.github.com/schemas/*.gschema.xml \
~/.local/share/glib-2.0/schemas/

glib-compile-schemas ~/.local/share/glib-2.0/schemas/

export XDG_DATA_DIRS="$HOME/.local/share:/usr/local/share:/usr/share"
```

Verify:

```bash
gsettings list-schemas | grep dash-to-panel
```

Expected:

```text
org.gnome.shell.extensions.dash-to-panel
```

## Allow and enable user extensions

```bash
gsettings set org.gnome.shell disable-user-extensions false
gnome-extensions enable dash-to-panel@jderose9.github.com
gnome-extensions disable ubuntu-dock@ubuntu.com
```

Check:

```bash
gnome-extensions info dash-to-panel@jderose9.github.com
```

The important lines should be:

```text
Enabled: Yes
State: ACTIVE
```

## Apply the top-panel look

```bash
gsettings set org.gnome.shell.extensions.dash-to-panel panel-position 'TOP'
gsettings set org.gnome.shell.extensions.dash-to-panel panel-size 30

gsettings set org.gnome.shell.extensions.dash-to-panel trans-use-custom-opacity true
gsettings set org.gnome.shell.extensions.dash-to-panel trans-panel-opacity 0.80

gsettings set org.gnome.shell.extensions.dash-to-panel appicon-margin 2
gsettings set org.gnome.shell.extensions.dash-to-panel appicon-padding 4
```

## Quick restore

```bash
gsettings set org.gnome.shell disable-user-extensions false
gnome-extensions enable dash-to-panel@jderose9.github.com
gnome-extensions disable ubuntu-dock@ubuntu.com

gsettings set org.gnome.shell.extensions.dash-to-panel panel-position 'TOP'
gsettings set org.gnome.shell.extensions.dash-to-panel panel-size 30
gsettings set org.gnome.shell.extensions.dash-to-panel trans-use-custom-opacity true
gsettings set org.gnome.shell.extensions.dash-to-panel trans-panel-opacity 0.80
gsettings set org.gnome.shell.extensions.dash-to-panel appicon-margin 2
gsettings set org.gnome.shell.extensions.dash-to-panel appicon-padding 4
```

## Notes

- Desktop environment: Ubuntu GNOME
- Dash to Panel extension ID: `dash-to-panel@jderose9.github.com`
- Ubuntu Dock extension ID: `ubuntu-dock@ubuntu.com`
