import json
import csv
from flask import Blueprint, request, session
from flask_cors import cross_origin
from database import MysqlSession
from uploads.models import WyomingCheckInfo
import pymysql
from uploads.wyoming import RoyaltyChecks
from notify import Email


uploads = Blueprint('uploads', 'uploads', url_prefix='/upload')


@uploads.route('/notify', methods=['POST'])
@cross_origin()
def send_email():
    data = request.get_json()
    msg = Email()
    ret = msg.send_email(data['sender'], data['recipient'], data['subject'], data['body'])
    return json.dumps(ret)


@uploads.route('/wyoming/royalty/clear', methods=['POST'])
@cross_origin()
def clear_royalty():
    obj = RoyaltyChecks()
    ret = obj.clear()
    return json.dumps(ret)


@uploads.route('/wyoming/royalty/insert', methods=['POST'])
@cross_origin()
def upload_royalty():
    obj = RoyaltyChecks()
    ret = obj.upload(request.data)
    return json.dumps(ret)


@uploads.route('/wyoming/royalty_raw', methods=['POST'])
@cross_origin()
def upload_royalty_raw():
    db = MysqlSession()
    strData = request.data.decode("utf-8")
    my_conn = pymysql.connect(host='10.5.24.72', port=3306, user='wyadmin', passwd='EOGWY_2017', db='wyoming')
    rows = strData.splitlines()
    i = 0
    for row in rows:
        if i < 10:
            print(row)
            i += 1
    my_cursor = my_conn.cursor()
    stmt = "INSERT INTO wyoming.wy_check_info "
    stmt += '(WLOWNR, check_date_year, check_date_month, check_date_day, '
    stmt += 'PRPRTY, PRPSUB, PRPDES, PRODYR, PRODMO, VOLUME, GRSVAL, BTUCONTENT, '
    stmt += 'WLINT, OWNNET, PRICE, MKT, COMMENTS, APINUM) '
    #stmt += " VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    stmt += ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, '
    stmt += '%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    print(stmt)
    my_cursor.executemany(stmt, rows)
    my_cursor.commit()
    return_dict = {}
    return_dict['msg'] = 'OK'
    return json.dumps(return_dict)


@uploads.route('/wyoming/royalty_pipe', methods=['POST'])
@cross_origin()
def upload_royalty_pipe():
    db = MysqlSession()
    strData = request.data.decode("utf-8")
    csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)
    reader = csv.DictReader(strData.splitlines(), dialect='piper')
    for row in reader:
        db.add(WyomingCheckInfo(**row))
    db.commit()
    db.close()
    return_dict = {}
    return_dict['msg'] = 'OK'
    return json.dumps(return_dict)


@uploads.route('/wyoming/royalty_json', methods=['POST'])
@cross_origin()
def upload_royalty_json():
    db = MysqlSession()
    data = request.get_json()
    rows = data['royalty']
    for row in rows:
        db.add(WyomingCheckInfo(**row))
    db.commit()
    db.close()
    return_dict = {}
    return_dict['msg'] = 'OK'
    return json.dumps(return_dict)


@uploads.route('/wyoming/getroyalty', methods=['POST'])
@cross_origin()
def retrieve_royalty():
    #print(request.data)
    session = MysqlSession()
    checks = session.query(WyomingCheckInfo).filter(WyomingCheckInfo.wlownr == 164)
    rs = []
    for check in checks:
        d = {}
        d['owner'] = str(check.wlownr)
        d['gross'] = str(check.grsval)
        rs.append(d)
    session.close()
    ret_val = json.dumps(rs)
    return ret_val
