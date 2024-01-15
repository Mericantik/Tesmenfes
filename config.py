import os
from dotenv import load_dotenv

# load from .env
load_dotenv(".env") #
DB_URL = os.getenv("DB_URL", 0).split()))

daget_claim_group = int(os.environ.get("DAGET_CLAIM_GROUP", -1001603368620))

# =========================================================== #

daget = 0
claimed = []

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_bfrent = 1
batas_gfrent = 1
batas_daddy_sugar = 1
batas_proplayer = 1
batas_talent = 3
batas_temancurhat = 3

# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "100"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "100"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "100"))
biaya_temancurhat = int(os.environ.get("BIAYA_TEMANCURHAT", "100"))
biaya_proplayer = int(os.environ.get("BIAYA_PROPLAYER", "100"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "100"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "100"))
biaya_delete = int(os.environ.get("BIAYA_DELETE", 25))

# =========================================================== #

hastag = os.environ.get("HASTAG", "#onsgirl #onsboy #onsrate #onstory").replace(" ", "|").lower()
kata_terlarang = os.environ.get("KATA_TERLARANG", "desah vcs bokep budak slave tocil horny callsex naked moan bbg coli jatah sgrbby bkp lecehin nakalin nen nenen kontol memek 18+ dick s*x sex t0cil fwb cum nsfw coli sugarbaby porn crot").replace(" ", "|").lower()

# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://t.me/statusonsbase/97")
pic_girl = os.environ.get("PIC_GIRL", "https://t.me/statusonsbase/98")

# =========================================================== #
top_up = os.environ.get("patuhi_ketentuan", "chat nazhak untuk membeli koin")
patuhi_ketentuan = os.environ.get("patuhi_ketentuan", "")
pesan_join = os.environ.get("PESAN_JOIN", "Tidak Dapat Diakses Harap Join Terlebih Dahulu")
start_msg = os.environ.get("START_MSG", "Hai {mention} 🌱\n\n<b>ONS BASE Bot</b> adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @ONSBASE Secara Anonymous. Untuk Bantuan Ketik /help")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:

{h1} / {h2} (Untuk Mencari Pasangan, Teman , Partner FWB)
{h3} (Untuk dirate)
{h4} (Untuk Berbagi Cerita)
""")
