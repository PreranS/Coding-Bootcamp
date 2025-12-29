DROP TABLE IF EXISTS
xray,
wearabledevicedata,
symptom,
ecgreport,
diseasedetail,
bloodtest,
cardiodiagnosis,
addressinfo,
memberinfo
CASCADE;

CREATE TABLE memberinfo (
  member_id VARCHAR(45) PRIMARY KEY,
  username VARCHAR(45),
  firstname VARCHAR(45),
  lastname VARCHAR(45),
  age INTEGER,
  gender VARCHAR(45),
  email VARCHAR(45),
  phonenumber BIGINT
);

CREATE TABLE addressinfo (
  address_id VARCHAR(45),
  city VARCHAR(45),
  state VARCHAR(45),
  country VARCHAR(45),
  pincode VARCHAR(45),
  memberinfo_member_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (address_id, memberinfo_member_id),
  CONSTRAINT fk_addressinfo_memberinfo
    FOREIGN KEY (memberinfo_member_id)
    REFERENCES memberinfo(member_id)
);
CREATE INDEX fk_addressinfo_memberinfo_idx
ON addressinfo(memberinfo_member_id);

CREATE TABLE cardiodiagnosis (
  cardio_id VARCHAR(45) PRIMARY KEY,
  cardioarrestdetected INTEGER,
  date TIMESTAMP,
  memberinfo_member_id VARCHAR(45) NOT NULL,
  CONSTRAINT fk_cardiodiagnosis_memberinfo
    FOREIGN KEY (memberinfo_member_id)
    REFERENCES memberinfo(member_id)
);

CREATE INDEX fk_cardiodiagnosis_memberinfo_idx
ON cardiodiagnosis(memberinfo_member_id);

CREATE TABLE bloodtest (
  blood_id VARCHAR(45),
  date TIMESTAMP,
  bloodpressure INTEGER,
  fbs INTEGER,
  thal INTEGER,
  serumcholesterol INTEGER,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (blood_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_bloodtest_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE INDEX fk_bloodtest_cardiodiagnosis_idx
ON bloodtest(cardiodiagnosis_cardio_id);

CREATE TABLE diseasedetail (
  disease_id VARCHAR(45),
  diagnoseddate TIMESTAMP,
  recovereddate TIMESTAMP,
  isrecovered INTEGER,   -- 0 = Not recovered, 1 = Recovered
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (disease_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_diseasedetail_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);


CREATE INDEX fk_diseasedetail_cardiodiagnosis_idx
ON diseasedetail(cardiodiagnosis_cardio_id);

CREATE TABLE ecgreport (
  ecg_id VARCHAR(45),
  date TIMESTAMP,
  restecg INTEGER,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (ecg_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_ecgreport_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE INDEX fk_ecgreport_cardiodiagnosis_idx
ON ecgreport(cardiodiagnosis_cardio_id);


CREATE TABLE symptom (
  symptom_id VARCHAR(45),
  date TIMESTAMP,
  exang INTEGER,
  oldpeak FLOAT,
  cp INTEGER,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (symptom_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_symptom_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE INDEX fk_symptom_cardiodiagnosis_idx
ON symptom(cardiodiagnosis_cardio_id);

CREATE TABLE wearabledevicedata (
  wearable_device_id VARCHAR(45),
  thalach INTEGER,
  slope INTEGER,
  date TIMESTAMP,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (wearable_device_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_wearabledevicedata_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE INDEX fk_wearabledevicedata_cardiodiagnosis_idx
ON wearabledevicedata(cardiodiagnosis_cardio_id);

CREATE TABLE xray (
  xray_id VARCHAR(45),
  date TIMESTAMP,
  ca INTEGER,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (xray_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_xray_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE INDEX fk_xray_cardiodiagnosis_idx
ON xray(cardiodiagnosis_cardio_id);





