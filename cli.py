import argparse
import subprocess
import logging

# Logger configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="[%(levelname)s] %(asctime)s - %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
)

def run_docker_compose(fileName:str):
  print("runing - docker-compose up")
  result = subprocess.run("docker-compose -f compose.dev.yml up -d", shell=True)

  if result.returncode != 0:
    print("Erro - ", result.stderr)
    return
  
  print("Done - docker-compose up")

def dev(args):
  
  match args.action:
    case "setup":
      logging.info("Start dev setup") 

    case "run":
      logging.info("Start dev run") 
    
    case "stop":
      logging.info("Start dev stop") 
    
    case "clear":
      logging.info("Start dev clear") 
    
    case _:
      logging.error("Dev arg not found") 

def prod(args):
  log = lambda message: print(f"[PROD] {message}")
  log("Work in progress")

def main():
  # Create the top-level parser
  parser = argparse.ArgumentParser( description="Project management tool")
  subparsers = parser.add_subparsers()

  # Create the parser for the "dev" command
  parser_dev = subparsers.add_parser('dev', help="Manage development environment")
  parser_dev.add_argument("action", choices=["setup","run", "stop", "clear"], help="Action to run in the development environment")
  parser_dev.set_defaults(func=dev)

  # Create the parser for the "prod" command
  parser_prod = subparsers.add_parser('prod', help="Manage production environment")
  parser_prod.set_defaults(func=prod)

  # Parse the args
  args = parser.parse_args()

  # Call help if no function is selected
  if not hasattr(args, "func"):
    parser.print_help();
    return

  # Call whatever function was selected
  args.func(args) 

if __name__ == "__main__":
  main();
  