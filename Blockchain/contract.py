import subprocess
from Blockchain import utils

CONTRACT_ADDRESS = "0xee471cd65d7158d1800576b9d072f49502f48499ee430ed4f1dbcc61b2209244"
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


def register_ai(user_address: str, creator_obj_address: str, ai_id: str, rag_hash: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::register_ai",
      "--args", f"address:{user_address}",
      f"address:{creator_obj_address}", f"String:{ai_id}", f"String:{rag_hash}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)

  return tx_hash
  
def store_embedding_data(user_address: str, creator_obj_address: str, ai_id: str, rag_hash: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::store_rag_hash_data",
      "--args", f"address:{user_address}",
      f"address:{creator_obj_address}", f"String:{ai_id}", f"String:{rag_hash}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)

  return tx_hash


def pay_for_usage(creator_obj_address: str, ai_id: str, consumer_obj_address, amount: int) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::pay_for_usage",
      "--args", f"address:{creator_obj_address}",
      f"String:{ai_id}", f"addresss:{consumer_obj_address}", f"u64:{amount}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)
  
  print("stdout:", stdout)
  print("stderr:", stderr)

  return tx_hash
  
def claim_rewards_by_ai(user_address: str, creator_obj_address: str, ai_id: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::claim_rewards_by_ai",
      "--args", f"address:{user_address}", f"address:{creator_obj_address}",
      f"String:{ai_id}"
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)
  
  return tx_hash

def request_faucet(consumer_obj_address: str) -> str:
  command = [
      "aptos", "move", "run",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::request_faucet",
      "--args", f"address:{consumer_obj_address}",
  ]
  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate(input="yes\n")
  tx_hash = utils.parse_and_get_tx_hash(stdout)

  print("stdout:", stdout)
  print("stderr:", stderr)
  
  return tx_hash
  # return ""


# View functions

def view_exists_creator_at(creator_obj_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::exists_creator_at",
      "--args", f"address:{creator_obj_address}"
  ]

def view_exists_consumer_at(consumer_obj_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::exists_consumer_at",
      "--args", f"address:{consumer_obj_address}"
  ]

def view_contain_ai(creator_obj_address: str, ai_id: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::contain_ai",
      "--args", f"address:{creator_obj_address}", f"String:{ai_id}"
  ]

def view_get_ai_rewards(creator_obj_address: str, ai_id: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::get_ai_rewards",
      "--args", f"address:{creator_obj_address}", f"String:{ai_id}"
  ]

def view_get_consumer_balance(consumer_obj_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::get_consumer_balance",
      "--args", f"address:{consumer_obj_address}"
  ]

def view_get_free_trial_count(consumer_obj_address: str):
  command = [
      "aptos", "move", "view",
      "--function-id", f"{CONTRACT_ADDRESS}::{MODULE}::get_free_trial_count",
      "--args", f"address:{consumer_obj_address}"
  ]

