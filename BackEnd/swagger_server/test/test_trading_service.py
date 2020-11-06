from swagger_server.models.stock_description import StockDescription
from swagger_server.models.stock_value import StockValue
from swagger_server.models.auth_key import AuthKey
from swagger_server.services import trading_service

description = StockDescription("AMZN", None, None, None, None, None, None, None, None, None, None)
auth_key = AuthKey(None, "Aj7LrIzhhciVLS1JgNCp9rAfCmseDOOgFf3mwGj9vMFYVZQ3aZ2sLB7jYW1x3B0VwWUnAYfjG846enNzVotw2ODixHqJz9JR0RpzwpmbZy44g39ci1vgaG9S9ObCFGKj", None)

# transaction = trading_service.buy_stock(auth_key, description, 10)
# print(transaction)