![Apache_Spark_logo](Apache_Spark_logo.png)

[**Apache Spark**](https://spark.apache.org/), büyük veri kümeleri üzerinde paralel olarak işlem yapılmasını sağlayan, Scala dili ile geliştirilmiş açık kaynak kodlu kütüphanedir.

Disk bazlı çalışma yapısına sahip olan “MapReduce”un oluşturduğu performans maliyetlerinin çözümüyle ortaya çıkan Spark, bellek içi veri işleme özelliğiyle büyük veri uygulamalarında Apache Hadoop’tan daha hızlı çalışabilmektedir.

```python3
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

parDF1 = spark.read.parquet("data/bdf6370f3c8e4182a97cd930996df1b7.snappy.parquet")

parDF1.printSchema()

"""
root
 |-- kind: string (nullable = true)
 |-- etag: string (nullable = true)
 |-- id: string (nullable = true)
 |-- snippet_channelid: string (nullable = true)
 |-- snippet_title: string (nullable = true)
 |-- snippet_assignable: boolean (nullable = true)
"""

parDF1.show(truncate = False)

"""
+---------------------+---------------------------------------------------------+---+------------------------+---------------------+------------------+
|kind                 |etag                                                     |id |snippet_channelid       |snippet_title        |snippet_assignable|
+---------------------+---------------------------------------------------------+---+------------------------+---------------------+------------------+
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/Xy1mB4_yLrHy_BmKmPBggty2mZQ"|1  |UCBR8-60-B28hp2BmDPdntcQ|Film & Animation     |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/UZ1oLIIz2dxIhO45ZTFR3a3NyTA"|2  |UCBR8-60-B28hp2BmDPdntcQ|Autos & Vehicles     |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/nqRIq97-xe5XRZTxbknKFVe5Lmg"|10 |UCBR8-60-B28hp2BmDPdntcQ|Music                |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/HwXKamM1Q20q9BN-oBJavSGkfDI"|15 |UCBR8-60-B28hp2BmDPdntcQ|Pets & Animals       |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/9GQMSRjrZdHeb1OEM1XVQ9zbGec"|17 |UCBR8-60-B28hp2BmDPdntcQ|Sports               |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/FJwVpGCVZ1yiJrqZbpqe68Sy_OE"|18 |UCBR8-60-B28hp2BmDPdntcQ|Short Movies         |false             |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/M-3iD9dwK7YJCafRf_DkLN8CouA"|19 |UCBR8-60-B28hp2BmDPdntcQ|Travel & Events      |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/WmA0qYEfjWsAoyJFSw2zinhn2wM"|20 |UCBR8-60-B28hp2BmDPdntcQ|Gaming               |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/EapFaGYG7K0StIXVf8aba249tdM"|21 |UCBR8-60-B28hp2BmDPdntcQ|Videoblogging        |false             |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/xId8RX7vRN8rqkbYZbNIytUQDRo"|22 |UCBR8-60-B28hp2BmDPdntcQ|People & Blogs       |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/G9LHzQmx44rX2S5yaga_Aqtwz8M"|23 |UCBR8-60-B28hp2BmDPdntcQ|Comedy               |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/UVB9oxX2Bvqa_w_y3vXSLVK5E_s"|24 |UCBR8-60-B28hp2BmDPdntcQ|Entertainment        |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/QiLK0ZIrFoORdk_g2l_XR_ECjDc"|25 |UCBR8-60-B28hp2BmDPdntcQ|News & Politics      |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/r6Ck6Z0_L0rG37VJQR200SGNA_w"|26 |UCBR8-60-B28hp2BmDPdntcQ|Howto & Style        |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/EoYkczo9I3RCf96RveKTOgOPkUM"|27 |UCBR8-60-B28hp2BmDPdntcQ|Education            |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/w5HjcTD82G_XA3xBctS30zS-JpQ"|28 |UCBR8-60-B28hp2BmDPdntcQ|Science & Technology |true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/SalkJoBWq_smSEqiAx_qyri6Wa8"|29 |UCBR8-60-B28hp2BmDPdntcQ|Nonprofits & Activism|true              |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/lL7uWDr_071CHxifjYG1tJrp4Uo"|30 |UCBR8-60-B28hp2BmDPdntcQ|Movies               |false             |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/WnuVfjO-PyFLO7NTRQIbrGE62nk"|31 |UCBR8-60-B28hp2BmDPdntcQ|Anime/Animation      |false             |
|youtube#videoCategory|"m2yskBQFythfE4irbTIeOgYYfBU/ctpH2hGA_UZ3volJT_FTlOg9M00"|32 |UCBR8-60-B28hp2BmDPdntcQ|Action/Adventure     |false             |
+---------------------+---------------------------------------------------------+---+------------------------+---------------------+------------------+
only showing top 20 rows
"""
```