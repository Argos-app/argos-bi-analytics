from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view(
    name="workspace.argos_bi.aplicacoes_lake_gold",
    comment="Dados de aplicações preparados para o dashboard",
)
def aplicacoes_gold():
    df = spark.table("workspace.argos_bi.aplicacoes_lake_silver")

    df = df.withColumn(
        "situacao_carencia",
        F.when(
            F.col("fim_carencia").isNull(),
            "Não informada",
        )
        .when(
            F.col("fim_carencia") > F.current_date(),
            "Em carência",
        )
        .otherwise("Encerrada"),
    )

    df = df.withColumn(
        "aplicacao_em_carencia",
        F.when(
            F.col("fim_carencia") > F.current_date(),
            1,
        ).otherwise(0),
    )

    return df
