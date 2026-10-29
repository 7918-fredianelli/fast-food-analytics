CREATE OR REPLACE VIEW FASTFOOD_DB.PUBLIC.VW_ORDER_METRICS AS
SELECT 
    ORDER_ID,
    CUISINE_TYPE,
    ORDER_VALUE,
    DELIVERY_TIME_MINUTES,
    
    -- Segmentação de valor do pedido (Ticket Alto vs Baixo)
    CASE 
        WHEN ORDER_VALUE >= 35 THEN 'High-Value'
        ELSE 'Standard'
    END AS ORDER_TIER,
    
    -- Eficiência da Entrega (Alerta de atraso hipotético > 30 min)
    CASE 
        WHEN DELIVERY_TIME_MINUTES > 30 THEN 'Delayed'
        ELSE 'On-Time'
    END AS DELIVERY_STATUS

FROM FASTFOOD_DB.PUBLIC.ORDERS_CLEANED;