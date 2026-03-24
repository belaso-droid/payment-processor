import os
import logging
from typing import Optional, Dict, Any
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path: str) -> Dict[str, Any]:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path, 'r') as file:
        return json.load(file)

def save_transaction(transaction_data: Dict[str, Any], output_dir: str) -> str:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"transaction_{timestamp}.json"
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_path, 'w') as file:
        json.dump(transaction_data, file, indent=4)
    
    logging.info(f"Transaction saved to {file_path}")
    return file_path

def validate_transaction(transaction_data: Dict[str, Any]) -> bool:
    required_fields = ["amount", "currency", "customer_id", "merchant_id"]
    
    for field in required_fields:
        if field not in transaction_data:
            logging.error(f"Missing required field: {field}")
            return False
    
    if not isinstance(transaction_data["amount"], (int, float)) or transaction_data["amount"] <= 0:
        logging.error("Invalid amount")
        return False
    
    return True

def generate_receipt(transaction_data: Dict[str, Any]) -> Dict[str, Any]:
    receipt = {
        "transaction_id": transaction_data.get("transaction_id", "N/A"),
        "amount": transaction_data["amount"],
        "currency": transaction_data["currency"],
        "customer_id": transaction_data["customer_id"],
        "merchant_id": transaction_data["merchant_id"],
        "timestamp": datetime.now().isoformat()
    }
    
    return receipt