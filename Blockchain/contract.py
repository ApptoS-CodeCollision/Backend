import subprocess
from Blockchain import utils
import json

CONTRACT_ADDRESS = "0x580372d1e6045e086b77adb704dc60fe227cc421d533dd7a4b265e42f72d5d44"
MODULE = "reward"

def register_user(user_address:str) -> {str, str}:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::register_user",
      "--args", f"address:{user_address}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  response = utils.get_transaction_by_hash(tx_hash=tx_hash)

  creator_obj_address = ''
  consumer_obj_address = ''

  if response.status_code == 200:
    for change in response.json()["changes"]:
      if change["data"] and "Creator" in change["data"]["type"]:
          creator_obj_address = change["address"]
      elif change["data"] and "Consumer" in change["data"]["type"]:
          consumer_obj_address = change["address"]

  print("creator_address:", creator_obj_address)
  print("consumer_address:", consumer_obj_address)

  return creator_obj_address, consumer_obj_address


def register_ai(creator_address: str,  ai_id: str, prompt: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::register_ai",
      "--args", f"address:{creator_address}", f"String:{ai_id}", f"String:{prompt}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)

  return tx_hash
  
def store_rag_data(creator_address: str, ai_id: str, prompt: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::store_rag_data",
      "--args", f"address:{creator_address}", f"String:{ai_id}", f"String:{prompt}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)

  return tx_hash


def pay_for_chat(creator_address: str, consumer_address :str, ai_id: str, amount: int) -> str:

  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::pay_for_chat",
      "--args", f"address:{creator_address}", f"address:{consumer_address}", f"String:{ai_id}", f"u64:{amount}"
  ]
  print(command)
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  print("stdout:", stdout)
  print("stderr:", stderr)
  tx_hash = utils.parse_and_get_tx_hash(stdout)
  


  return tx_hash
  
def claim_rewards_by_ai(user_address: str, ai_id: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::claim_ai_rewards_by_creator",
      "--args", f"address:{user_address}", f"String:{ai_id}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)
  
  return tx_hash

def request_faucet(user_address: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::request_faucet",
      "--args", f"address:{user_address}",
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)
  
  return tx_hash

def use_free_trial(consumer_obj_address: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::use_free_trial",
      "--args", f"address:{consumer_obj_address}",
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)
  
  return tx_hash


# View functions

def view_exists_creator_at(creator_obj_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::exists_creator_at",
      "--args", f"address:{creator_obj_address}"
  ]
  result = subprocess.run(command, capture_output=True, text=True)
  json_output = json.loads(result.stdout)
  print(json_output)
  return str(json_output["Result"][0])


def view_exists_consumer_at(consumer_obj_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::exists_consumer_at",
      "--args", f"address:{consumer_obj_address}"
  ]
  result = subprocess.run(command, capture_output=True, text=True)
  json_output = json.loads(result.stdout)
  print(json_output)
  return str(json_output["Result"][0])

def view_contain_ai(creator_obj_address: str, ai_id: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::contain_ai",
      "--args", f"address:{creator_obj_address}", f"String:{ai_id}"
  ]
  result = subprocess.run(command, capture_output=True, text=True)
  json_output = json.loads(result.stdout)
  print(json_output)
  return str(json_output["Result"][0])

def view_get_ai_rewards(creator_obj_address: str, ai_id: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::get_ai_rewards",
      "--args", f"address:{creator_obj_address}", f"String:{ai_id}"
  ]
  result = subprocess.run(command, capture_output=True, text=True)
  json_output = json.loads(result.stdout)
  print(json_output)
  return str(json_output["Result"][0])

def view_get_consumer_balance(consumer_obj_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::get_consumer_balance",
      "--args", f"address:{consumer_obj_address}"
  ]
  result = subprocess.run(command, capture_output=True, text=True)
  json_output = json.loads(result.stdout)
  print(json_output)
  return str(json_output["Result"][0])

def view_get_free_trial_count(user_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::get_free_trial_count",
      "--args", f"address:{user_address}"
  ]
  result = subprocess.run(command, capture_output=True, text=True)
  json_output = json.loads(result.stdout)
  print(json_output)
  return str(json_output["Result"][0])

