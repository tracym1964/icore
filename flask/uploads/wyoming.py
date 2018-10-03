import csv
from database import MysqlSession
from uploads.models import WyomingCheckInfo
import pymysql
from notify import Email


class RoyaltyChecks:
    """
    Upload class for transferring Wyoming royalty checks to MySQL from DB/2
    """

    def __init__(self):
        """ method to upload Wyoming royalty file from DB/2 to MySQL """
        self.conn = pymysql.connect(host='10.5.24.72', port=3306, user='wyadmin', passwd='EOGWY_2017', db='wyoming')
        self.my_cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    # create function to send email
    def clear(self):
        response = {}
        try:
            self.my_cursor.execute("TRUNCATE TABLE WY_CHECK_INFO")
            response['msg'] = 'OK'
        except:
            response['msg'] = 'Truncate table operation failed'
        finally:
            self.my_cursor.close()
        return response

    def upload(self, data):
        """
        method to upload Wyoming royalty file from DB/2 to MySQL
        """
        response = {}
        str_data = data.decode("utf-8")
        csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)
        reader = csv.DictReader(str_data.splitlines(), dialect='piper')
        wyoming = []
        for row in reader:
            wyoming.append((
                row['WLOWNR'],
                row['CHECK_DATE_YEAR'],
                row['CHECK_DATE_MONTH'],
                row['CHECK_DATE_DAY'],
                row['PRPRTY'],
                row['PRPSUB'],
                row['PRPDES'],
                row['PRODYR'],
                row['PRODMO'],
                row['VOLUME'],
                row['GRSVAL'],
                row['BTUCONTENT'],
                row['WLINT'],
                row['OWNNET'],
                row['PRICE'],
                row['MKT'],
                row['COMMENTS'],
                row['APINUM']
            ))
        q = """ insert ignore into wyoming.wy_check_info (
                WLOWNR, CHECK_DATE_YEAR, CHECK_DATE_MONTH, CHECK_DATE_DAY, PRPRTY, PRPSUB,
                PRPDES, PRODYR, PRODMO, VOLUME, GRSVAL, BTUCONTENT, WLINT, OWNNET, PRICE,
                MKT, COMMENTS, APINUM) 
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
            """
        try:
            self.my_cursor.executemany(q, wyoming)
            self.conn.commit()
            response['msg'] = 'OK'
        except pymysql.DatabaseError as e:
            self.conn.rollback()
            response['msg'] = 'Commit failed'

        finally:
            self.my_cursor.close()
        return response

