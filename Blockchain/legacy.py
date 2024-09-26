import asyncio
from aptos_sdk.account import Account, AccountAddress
from aptos_sdk.async_client import FaucetClient, RestClient
from aptos_sdk.authenticator import Authenticator, FeePayerAuthenticator
from aptos_sdk.bcs import Serializer
from aptos_sdk.type_tag import TypeTag
from aptos_sdk.transactions import (
    EntryFunction,
    FeePayerRawTransaction,
    SignedTransaction,
    TransactionArgument,
    TransactionPayload,
)

import subprocess
from dotenv import load_dotenv

load_dotenv()

def recharge_consumer_balance_for_testing(consumer_obj_address:str):
  command = [
      "aptos", "move", "run",
      "--function-id", "0xee471cd65d7158d1800576b9d072f49502f48499ee430ed4f1dbcc61b2209244::reward::recharge_consumer_balance",
      "--args", f"address:{consumer_obj_address}",
  ]

  process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  stdout, stderr = process.communicate(input="yes\n")

  # 출력 결과 확인
  print("stdout:", stdout)
  print("stderr:", stderr)

async def register_user_legacy():
  NODE_URL = "https://api.testnet.aptoslabs.com/v1"

  MODULE_OWNER_PRIV_KEY = ""
  MODULE_OWNER_ADDRESS = "0xee471cd65d7158d1800576b9d072f49502f48499ee430ed4f1dbcc61b2209244"

  CONTRACT_ADDRESS = "0xee471cd65d7158d1800576b9d072f49502f48499ee430ed4f1dbcc61b2209244"
  MODULE_NAME = "reward"
  rest_client = RestClient(NODE_URL)

  module_owner_account = Account.load_key(MODULE_OWNER_PRIV_KEY)
  user_account_address = AccountAddress.from_str(user_address)

  transaction_arguments = [
      TransactionArgument(user_account_address, Serializer.struct),
  ]

  payload = EntryFunction.natural(
      f"{CONTRACT_ADDRESS}::{MODULE_NAME}",
      "register_user",
      [],
      transaction_arguments,
  )

  sequence_number = await rest_client.account_sequence_number(module_owner_account.address())

  signed_transaction = await rest_client.create_bcs_signed_transaction(
    sender=module_owner_account, 
    payload=payload,
    sequence_number=sequence_number
  )
  print(signed_transaction)

  tx_hash = await rest_client.submit_bcs_transaction(signed_transaction) # this doesn't work
  # await rest_client.wait_for_transaction(tx_hash)
  print(1)
  