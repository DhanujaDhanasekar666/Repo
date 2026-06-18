from app import transaction_status

def test_transaction_status():
    assert transaction_status() == "Transaction Validated Successfully"
