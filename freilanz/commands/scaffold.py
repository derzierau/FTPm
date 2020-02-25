from freilanz.config import Config
from freilanz.helper import make_dirs


def scaffold(click):
    config = Config()
    
    if config.config:
        root_dir = config.config['base']['user']['environment']['root_dir']
        # print(root_dir['environment'])
        if 'profiles' in config.config:
          for profile in config.config['profiles']:
            if 'projects' in profile:
              make_dirs(profile['projects'], f"{root_dir}/{profile['id']}", exist_ok=True)
            
    else:
        sec_path = click.prompt(
            'Not able to find config file within file tree. Please provide a path:')
