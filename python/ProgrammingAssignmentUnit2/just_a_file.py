def approve_forex_trade(customer_type, trade_amount, has_documentation):
    # Guard clause handles simplest rejection case first
    if customer_type != "corporate":
        return "Retail customers cannot trade forex"
    
    # Boolean expression combines conditions on single level
    if trade_amount <= 1000000 or has_documentation:
        return "Approved"
    
    return "Documentation required"
