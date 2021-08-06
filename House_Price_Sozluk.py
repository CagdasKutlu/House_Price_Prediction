#  0   Id             1460 non-null   int64     # Satışa dahil olan konut türünü tanımlar.
#  1   MSSubClass     1460 non-null   int64     # Satışın genel imar sınıflamasını tanımlar. KONUT TÜRÜ: 1946 yılından önce veya sonra yapılmış, dubkleks stil gibi
#  2   MSZoning       1460 non-null   object    # Konut tipi
#  3   LotFrontage    1201 non-null   float64   # Mülkün caddeye bakan cephesinin metre uzunluğu
#  4   LotArea        1460 non-null   int64     # Metrekare cinsinden arsa büyüklüğü
#  5   Street         1460 non-null   object    # Mülke giden cadde
#  6   Alley          91 non-null    object     # Sokak dar yol patika
#  7   LotShape       1460 non-null   object    # Mülkün genel şekli
#  8   LandContour    1460 non-null   object    # Arsa şekli yokuş düz
#  9   Utilities      1460 non-null   object    # Kullanılabilir yardımcı programlar elektrik gas su
#  10  LotConfig      1460 non-null   object    # Arsa yapısı içeride- köşede- çıkmaz sokak- 2 cephesi yola bakıyor
#  11  LandSlope      1460 non-null   object    # Eğim  hafif orta şiddetli
#  12  Neighborhood   1460 non-null   object    # Mahalle
#  13  Condition1     1460 non-null   object    # Çeşitli yakın olduğu yerler demiryolu otoyol, park vb
#  14  Condition2     1460 non-null   object    # Yakın olduğu birden fazla varsa
#  15  BldgType       1460 non-null   object    # Mülk tipi müstakil - dubleks - şehir evi
#  16  HouseStyle     1460 non-null   object    # Konut tarzı : katsayısı
#  17  OverallQual    1460 non-null   int64     # Evin malzeme kalitesi 1 2 3 4 5 6 78 9 10
#  18  OverallCond    1460 non-null   int64     # Evin genel durumu 1 2 3 4 5 6 78 9 10
#  19  YearBuilt      1460 non-null   int64     # Yapım yılı
#  20  YearRemodAdd   1460 non-null   int64     # Tadilat tarihi (tadilat veya ilave yapılmamışsa inşaat tarihi ile aynı)
#  21  RoofStyle      1460 non-null   object    # Çatı tipi - üçgen- düz kat- ahır tipi
#  22  RoofMatl       1460 non-null   object    # Çatı malzemesi metal membran ahşap fayans çakıl
#  23  Exterior1st    1460 non-null   object    # Evin dış kaplması çimento- tuğla - taş- sıva vs.
#  24  Exterior2nd    1460 non-null   object    # Birden fazlaysa 2. malzeme
#  25  MasVnrType     1452 non-null   object    # Duvar kaplama malzemesi tuğla- taş - kül bloğu
#  26  MasVnrArea     1452 non-null   float64   # Metrekare cinsinden duvar kaplama alanı üstteki yoksa 0
#  27  ExterQual      1460 non-null   object    # Dış cephedeki malzeme kalitesi değerlendirmesi ex: excellent,po: poor, TA: ortalama
#  28  ExterCond      1460 non-null   object    # Malzemenin dış cephedeki mevcut durumunu ex-gd-ta-da-po
#  29  Foundation     1460 non-null   object    # Temel tipi  BrkTil: Tuğla kiremit, PConc: Beton
#  30  BsmtQual       1423 non-null   object    # *** NA BODRUM YOK *** Bodrumun yüksekliği ex 100+ inç - po: <70 inç
#  31  BsmtCond       1423 non-null   object    # *** NA BODRUM YOK *** Dışarı çıkma veya bahçe seviyesindeki duvarları ifade eder. gd: Good , No :Tespit edilmedi
#  32  BsmtExposure   1422 non-null   object    # *** NA BODRUM YOK *** Bodrum katının genel durumu excellent-poor Fa-> nem çatlama, Po: Şiddetli nem
#  33  BsmtFinType1   1423 non-null   object    # *** NA BODRUM YOK *** Bodrum yaşam alanı değerlendirmesi GLQ : İyi Y.A. , Rec : Dinlenme odası, Unf: Bitmemiş
#  34  BsmtFinSF1     1460 non-null   float64   # Bitmiş metrekare
#  35  BsmtFinType2   1422 non-null   object    # *** NA BODRUM YOK *** Bodrum bitmiş alanın derecelendirmesi (birden fazla tip varsa) GLQ : İyi Y.A., BLQ: Ortalama altı
#  36  BsmtFinSF2     1460 non-null   float64   # Bitmiş metrekare
#  37  BsmtUnfSF      1460 non-null   float64   # Bitmemiş metrekarelik bodrum alanı
#  38  TotalBsmtSF    1460 non-null   float64   # Bodrum alanının toplam metrekaresi
#  39  Heating        1460 non-null   object    # Isıtma türü Floor: Yerden, GasA: Gazlı havalndırma,
#  40  HeatingQC      1460 non-null   object    # Isıtma kalitesi ve durumu excellent - poor
#  41  CentralAir     1460 non-null   object    # *** YES- NO *** Merkezi Isıtma
#  42  Electrical     1459 non-null   object    # Elektrik sistemi - SBrkr:Standart Devre Kesiciler ve Romex
#  43  1stFlrSF       1460 non-null   int64     # 1. kaç metrekaresi
#  44  2ndFlrSF       1460 non-null   int64     # 2. Kat metrekaresi
#  45  LowQualFinSF   1460 non-null   int64     # Düşük kaliteli bitmiş metrekare
#  46  GrLivArea      1460 non-null   int64     # Zemin üstü yaşam alanı
#  47  BsmtFullBath   1460 non-null   float64   # Bodrum katı banyoları
#  48  BsmtHalfBath   1460 non-null   float64   # Bodrum yarım banyoları
#  49  FullBath       1460 non-null   int64     # Banyo
#  50  HalfBath       1460 non-null   int64     # Tuvalet
#  51  BedroomAbvGr   1460 non-null   int64     # Zemin üstü Yatak odası (bodrum dahil değil)
#  52  KitchenAbvGr   1460 non-null   int64     # Zemin üstü mutfak
#  53  KitchenQual    1460 non-null   object    # Mutfak kalitesi Excellent- poor
#  54  TotRmsAbvGrd   1460 non-null   int64     # Zemin üstü toplam yatak odası
#  55  Functional     1460 non-null   object    # Ev işlevselliği Min1: Küçük kesinti, Sev : Ağır hasarlı
#  56  Fireplaces     1460 non-null   int64     # Şömine sayısı
#  57  FireplaceQu    770 non-null    object    # *** NA Şömine YOK ***Şömine kalitesi Excellent - Poor
#  58  GarageType     1379 non-null   object    # *** NA Garaj YOK ***Garaj tipi 2Types : 2 tipten fazla, Attchd:Eve bağlı,
#  59  GarageYrBlt    1379 non-null   float64   # Garajın yapıldığı yıl
#  60  GarageFinish   1379 non-null   object    # *** NA Garaj YOK *** Garajın İnşa Durumu Fin : bitmiş, RFn: Kabası bitmiş
#  61  GarageCars     1460 non-null   float64   # Garajın araç kapasitesi cinsinden boyutu
#  62  GarageArea     1460 non-null   float64   # Garajın metrekaresi
#  63  GarageQual     1379 non-null   object    # Garaj Kalitesi Excellent - Poor
#  64  GarageCond     1379 non-null   object    # *** NA Garaj YOK *** Garaj durumu Excellent-Poor
#  65  PavedDrive     1460 non-null   object    # Asfaltlanmış araba yolu Y: Kaplamalı , P: Kısmi Kaplama, N: Çakıl
#  66  WoodDeckSF     1460 non-null   int64     # Metrekare cinsinden ahşap balkon alanı
#  67  OpenPorchSF    1460 non-null   int64     # Metrekare cinsinden açık sundurma alanı
#  68  EnclosedPorch  1460 non-null   int64     # Metrekare cinsinden kapalı sundurma alanı
#  69  3SsnPorch      1460 non-null   int64     # Metrekare cinsinden üç mevsimlik sundurma alanı- kış bahçesi
#  70  ScreenPorch    1460 non-null   int64     # Metrekare cinsinden camlı kapalı alan
#  71  PoolArea       1460 non-null   int64     # Metrekare cinsinden havuz alanı
#  72  PoolQC         7 non-null      object    # *** NA HAVUZ YOK *** POOR YOK *** Havuz kalitesi excellent, good, ortalama, Fair , NA
#  73  Fence          281 non-null    object    # *** NA ÇİT YOK *** Çit kalitesi Gdprv: İyi gizlilik, GdWo : İyi Ahşap
#  74  MiscFeature    54 non-null     object    # *** NA ÖZELLİK YOK ***  Diğer kategorilerde kapsanmayan çeşitli özellik ASANSÖR,2. GARAJ, TENİS KORTU , MALZEMELİK(SHED)
#  75  MiscVal        1460 non-null   int64     # Çeşitli özelliğin $ Değeri
#  76  MoSold         1460 non-null   int64     # Satılığa çıktıktan sonra geçen ay süresi ?????????????
#  77  YrSold         1460 non-null   int64     # Satılan yıl
#  78  SaleType       1460 non-null   object    # Satış Türü WD: Geleneksel, CWD: Nakit,ConLI: Sözleşmeli düşük faiz, Oth: Diğer
#  79  SaleCondition  1460 non-null   object    # SAtış Durumu Normal ,Abnorml: Ticaret,haciz....
#  80  SalePrice      1460 non-null   int64     # Satış fiyatı