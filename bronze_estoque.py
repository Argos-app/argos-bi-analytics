from pyspark import pipelines as dp


@dp.materialized_view(
    name="workspace.argos_bi.estoque_lake_bronze",
    comment="Movimentações de estoque lidas do banco Argos",
)
def estoque_bronze():
    df = spark.sql("""
        SELECT
            sm.id AS movimentacao_id,
            sm.movement_date AS data_movimentacao,
            sm.type AS tipo_movimentacao,
            sm.reason AS motivo,

            mb.id AS lote_medicamento_id,
            mb.batch_number AS lote_medicamento,
            mb.expiry_date AS validade,

            m.id AS medicamento_id,
            m.brand_name AS medicamento,
            m.unit AS unidade,

            sm.quantity AS quantidade

        FROM dbArgos_catalog.public.stock_movement sm

        JOIN dbArgos_catalog.public.medicine_batch mb
            ON sm.medicine_batch_id = mb.id

        JOIN dbArgos_catalog.public.medicine m
            ON mb.medicine_id = m.id
    """)

    return df
