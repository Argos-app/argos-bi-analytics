from pyspark import pipelines as dp


@dp.materialized_view(
    name="workspace.argos_bi.estoque_lake_gold",
    comment="Movimentações de estoque preparadas para o dashboard",
)
def estoque_gold():
    df = spark.table("workspace.argos_bi.estoque_lake_silver")

    return df
