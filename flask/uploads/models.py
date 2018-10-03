from sqlalchemy import Table, Column, Integer, String, Date, Time, DECIMAL
from sqlalchemy.orm import mapper
from database import MysqlSession, Base


class WyomingCheckInfo(Base):
    """
    Define Wyoming Royalty check information table
    """
    __tablename__ = 'wy_check_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    wlownr = Column(DECIMAL(6, 0))
    check_date_year = Column(DECIMAL(4, 0))
    check_date_month = Column(DECIMAL(2, 0))
    check_date_day = Column(DECIMAL(2, 0))
    prprty = Column(DECIMAL(6, 0))
    prpsub = Column(String(3))
    prpdes = Column(String(30))
    prodyr = Column(DECIMAL(4, 0))
    prodmo = Column(DECIMAL(4, 0))
    volume = Column(DECIMAL(11, 2))
    grsval = Column(DECIMAL(11, 2))
    btucontent = Column(DECIMAL(15, 3))
    wlint = Column(DECIMAL(9, 8))
    ownnet = Column(DECIMAL(11, 2))
    price = Column(DECIMAL(6, 3))
    mkt = Column(String(19))
    comments = Column(String(47))
    apinum = Column(DECIMAL(12, 0))

    query = MysqlSession.query_property()

    def __init__(self, WLOWNR, CHECK_DATE_YEAR, CHECK_DATE_MONTH, CHECK_DATE_DAY, PRPRTY, PRPSUB,
                 PRPDES, PRODYR, PRODMO, VOLUME, GRSVAL, BTUCONTENT, WLINT, OWNNET, PRICE, MKT, COMMENTS, APINUM):
        self.wlownr = WLOWNR
        self.check_date_year = CHECK_DATE_YEAR
        self.check_date_month = CHECK_DATE_MONTH
        self.check_date_day = CHECK_DATE_DAY
        self.prprty = PRPRTY
        self.prpsub = PRPSUB
        self.prpdes = PRPDES
        self.prodyr = PRODYR
        self.prodmo = PRODMO
        self.volume = VOLUME
        self.grsval = GRSVAL
        self.btucontent = BTUCONTENT
        self.wlint = WLINT
        self.ownnet = OWNNET
        self.price = PRICE
        self.mkt = MKT
        self.comments = COMMENTS
        self.apinum = APINUM

    def __repr__(self):
        return 'Wyoming Royalty Payment Checks'