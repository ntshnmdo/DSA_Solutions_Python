from collections import defaultdict

def fraud_detection(non_fraud_codes, fraud_codes, mcc_thresholds, merchant_mccs, min_transactions, charges):
    # Parsing inputs
    non_fraud_set = set(non_fraud_codes.split(","))
    fraud_set = set(fraud_codes.split(","))
    
    mcc_dict = {mcc: float(threshold) for mcc, threshold in (line.split(",") for line in mcc_thresholds.split("\n"))}
    merchant_mcc_dict = {account: mcc for account, mcc in (line.split(",") for line in merchant_mccs.split("\n"))}
    min_transactions = int(min_transactions)
    
    merchant_tx_count = defaultdict(int)
    merchant_fraud_count = defaultdict(int)
    charge_fraud_status = {}
    merchant_fraudulent = set()

    # Process charges
    for charge in charges.split("\n"):
        parts = charge.split(",")
        
        if parts[0] == "CHARGE":
            _, charge_id, account_id, _, code = parts
            merchant_tx_count[account_id] += 1
            is_fraudulent = code in fraud_set
            charge_fraud_status[charge_id] = (account_id, is_fraudulent)
            
            if is_fraudulent:
                merchant_fraud_count[account_id] += 1
            
            # Check for minimum transaction count before evaluating
            if merchant_tx_count[account_id] >= min_transactions:
                mcc = merchant_mcc_dict[account_id]
                threshold = mcc_dict[mcc]
                
                # Check whether the threshold is a count or a percentage
                if threshold >= 1:  # Integer threshold
                    if merchant_fraud_count[account_id] >= threshold:
                        merchant_fraudulent.add(account_id)
                else:  # Percentage threshold
                    fraud_ratio = merchant_fraud_count[account_id] / merchant_tx_count[account_id]
                    if fraud_ratio >= threshold:
                        merchant_fraudulent.add(account_id)

        elif parts[0] == "DISPUTE":
            _, charge_id = parts
            if charge_id in charge_fraud_status:
                account_id, was_fraudulent = charge_fraud_status[charge_id]
                if was_fraudulent:
                    # Adjust fraud count upon dispute
                    merchant_fraud_count[account_id] -= 1
                    
                    # Recalculate fraud ratio or count
                    mcc = merchant_mcc_dict[account_id]
                    threshold = mcc_dict[mcc]
                    fraud_ratio = merchant_fraud_count[account_id] / merchant_tx_count[account_id]
                    
                    # Remove merchant from fraudulent list if criteria are no longer met
                    if (threshold >= 1 and merchant_fraud_count[account_id] < threshold) or \
                       (threshold < 1 and fraud_ratio < threshold):
                        merchant_fraudulent.discard(account_id)

    # Return lexicographically sorted list of fraudulent merchants
    return sorted(merchant_fraudulent)

# Example Input for a combined test case
non_fraud_codes = "approved,invalid_pin,expired_card"
fraud_codes = "do_not_honor,stolen_card,lost_card"
mcc_thresholds = "retail,0.8\nvenue,0.25"
merchant_mccs = "acct_1,retail\nacct_2,retail"
min_transactions = "2"
charges = """CHARGE,ch_1,acct_1,100,do_not_honor
CHARGE,ch_2,acct_1,200,lost_card
CHARGE,ch_3,acct_1,300,do_not_honor
DISPUTE,ch_2
CHARGE,ch_4,acct_2,400,lost_card
CHARGE,ch_5,acct_2,500,lost_card
CHARGE,ch_6,acct_1,600,lost_card
CHARGE,ch_7,acct_2,700,lost_card
CHARGE,ch_8,acct_2,800,do_not_honor"""

# Return the list of fraudulent merchants
result = fraud_detection(non_fraud_codes, fraud_codes, mcc_thresholds, merchant_mccs, min_transactions, charges)
print(result)  # This print is for checking the result, not part of the return statement
