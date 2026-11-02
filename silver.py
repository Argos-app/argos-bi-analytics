from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view(
    name="workspace.argos_bi.aplicacoes_lake_silver",
    comment="Dados de aplicações com identificador e data preenchidos",
)
def aplicacoes_silver():
    df = spark.table("workspace.argos_bi.aplicacoes_lake_bronze")

    df = df.filter(F.col("aplicacao_id").isNotNull())
    df = df.filter(F.col("data_aplicacao").isNotNull())

    return df
