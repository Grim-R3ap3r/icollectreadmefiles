#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "../stockExchange.h"

using namespace std;

TEST_CASE("Risk Server")
{
    StockExchange stockExchange(20, 15);
    NewOrder newOrder = {1, 1, 1, 10, 10, 'B'};
    int userId = 1;
    REQUIRE(stockExchange.newOrder(newOrder, userId) == true);
    newOrder = {1, 2, 2, 15, 9, 'S'};
    REQUIRE(stockExchange.newOrder(newOrder, userId) == true);
    newOrder = {1, 2, 3, 4, 8, 'B'};
    REQUIRE(stockExchange.newOrder(newOrder, userId) == true);
    newOrder = {1, 2, 4, 20, 8, 'B'};
    REQUIRE(stockExchange.newOrder(newOrder, userId) == false);
    Trade trade = {4, 2, 3, -4, 1};
    stockExchange.tradeInstrument(trade, userId);
    DeleteOrder deleteOrder = {2, 3};
    stockExchange.deleteOrder(deleteOrder, userId);
}
