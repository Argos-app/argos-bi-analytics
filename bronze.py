from pyspark import pipelines as dp


@dp.materialized_view(
    name="workspace.argos_bi.aplicacoes_lake_bronze",
    comment="Dados de aplicações lidos do banco Argos",
)
def aplicacoes_bronze():
    df = spark.sql("""
        SELECT
            a.id AS aplicacao_id,
            a.application_date AS data_aplicacao,

            p.id AS propriedade_id,
            p.name AS propriedade,
            p.city AS cidade,
            p.state AS estado,

            l.id AS lote_id,
            l.lot_code AS codigo_lote,
            l.category AS categoria_lote,
            l.is_exception_lot AS lote_excecao,

            mb.id AS lote_medicamento_id,
            mb.batch_number AS lote_medicamento,

            m.id AS medicamento_id,
            m.brand_name AS medicamento,
            tc.name AS categoria_medicamento,

            a.head_count_applied AS cabecas_aplicadas,
            a.route AS via_aplicacao,
            a.meat_withdrawal_end AS fim_carencia

        FROM dbArgos_catalog.public.application a

        JOIN dbArgos_catalog.public.lot l
            ON a.lot_id = l.id

        JOIN dbArgos_catalog.public.herd h
            ON l.herd_id = h.id

        JOIN dbArgos_catalog.public.property p
            ON h.property_id = p.id

        JOIN dbArgos_catalog.public.medicine_batch mb
            ON a.medicine_batch_id = mb.id

        JOIN dbArgos_catalog.public.medicine m
            ON mb.medicine_id = m.id

        JOIN dbArgos_catalog.public.therapeutic_category tc
            ON m.therapeutic_category_id = tc.id

        WHERE a.active = true
    """)

    return df
