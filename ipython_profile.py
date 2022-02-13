from pathlib import Path, PurePath
import subprocess
import click

_INIT_FILES = {
    PurePath('ipython_config.py'): (
"""
## lines of code to run at IPython startup.
#  Default: []
c.InteractiveShellApp.exec_lines = [
    '%autoreload 2'
]

## A list of dotted module names of IPython extensions to load.
#  Default: []
c.InteractiveShellApp.extensions = ['autoreload', 'ipython_autoimport']
"""
    )
}


def _echo(text):
    click.echo(f'[ipython-profile] {text}')


@click.command()
@click.option('--profile-dir',
              default='./.ipython-profile', help='Path to created')
def run(profile_dir):
    profile_dir = Path(profile_dir)
    if profile_dir.is_file():
        _echo('--profile-dir can\'t be a file.')
        return

    if not profile_dir.exists():
        profile_dir.mkdir()
        for filename, content in _INIT_FILES.items():
            (profile_dir / filename).write_text(content)
        _echo('Created .ipython-profile directory with default config.')

        project_directory = profile_dir.parent
        git_related = (
            (project_directory / PurePath('.git')).exists() or
            (project_directory / PurePath('.gitignore')).exists()
        )
        if git_related:
            _echo(
                'It seems that you are using git in this project. '
                'Consider adding .ipython-profile to .gitignore.'
            )

    subprocess.call(['ipython', '--profile-dir', str(profile_dir)])
