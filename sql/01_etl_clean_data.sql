CREATE OR REPLACE TABLE FASTFOOD_DB.PUBLIC.ORDERS_CLEANED AS
SELECT 
    ORDER_ID,
    ORDER_TIME,
    
    -- 1. Padronização de Texto: Removendo espaços extras e uniformizando letras maiúsculas/minúsculas da cidade e cozinha.
    INITCAP(TRIM(CITY)) AS CITY,
    INITCAP(TRIM(CUISINE_TYPE)) AS CUISINE_TYPE,
    
    -- 2. Consistência Financeira: Protegendo contra valores negativos e arredondando para 2 casas decimais.
    CASE 
        WHEN ORDER_VALUE < 0 THEN 0 
        ELSE ROUND(ORDER_VALUE, 2) 
    END AS ORDER_VALUE,
    
    -- 3. Tratamento de Anomalias no Tempo de Entrega: Convertendo tempos absurdos ou negativos em nulos.
    CASE 
        WHEN DELIVERY_TIME_MINUTES < 0 OR DELIVERY_TIME_MINUTES > 300 THEN NULL 
        ELSE DELIVERY_TIME_MINUTES 
    END AS DELIVERY_TIME_MINUTES,
    
    -- 4. Padronização de Pagamentos: Convertendo tudo para letras maiúsculas.
    UPPER(TRIM(PAYMENT_METHOD)) AS PAYMENT_METHOD,
    
    ITEMS_COUNT
    -- 5. Garantindo que ignore linhas sem o identificador de pedido.
FROM FASTFOOD_DB.PUBLIC.ORDERS
WHERE ORDER_ID IS NOT NULL; 