from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view(
    name="workspace.argos_bi.estoque_lake_silver",
    comment="Movimentações de estoque com identificação e data",
)
def estoque_silver():
    df = spark.table("workspace.argos_bi.estoque_lake_bronze")

    df = df.filter(F.col("movimentacao_id").isNotNull())
    df = df.filter(F.col("data_movimentacao").isNotNull())

    return df
