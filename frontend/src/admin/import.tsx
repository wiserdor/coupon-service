//@ts-nocheck
import React, { useState, useEffect } from 'react';
import Button from '@material-ui/core/Button';
import GetAppIcon from '@material-ui/icons/GetApp';
import { connect } from 'react-redux';
import { parse as convertFromCSV } from 'papaparse';
import { useRefresh } from 'react-admin';

const ImportButton = (props: any) => {
  const refresh = useRefresh();
  const { resource, dispatch, basePath } = props;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files && e.target.files[0];

    if (file) {
      convertFromCSV(file, {
        delimiter: ',',
        complete: (result) => {
          const { data } = result;

          const keys: string[] = data[0];
          const primaryKey = keys[0];

          const values = data.slice(1).map((row) => {
            const value: any = {};

            keys.forEach((key, index) => {
              value[key] = row[index];
            });

            return value;
          });
          values.forEach((v) => {
            fetch('/api/v1/vendors', {
              method: 'POST',
              headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                authorization: 'Bearer ' + localStorage.getItem('token'),
              },
              body: JSON.stringify(v),
            }).then(()=>refresh());
          });
        },
      });
    }
  };

  return (
    <>
      <input
        type="file"
        id="text-button-file"
        style={{ display: 'none' }}
        accept=".csv"
        onChange={handleChange}
      />
      <label
        htmlFor="text-button-file"
        style={{ display: 'inline-flex', alignItems: 'center' }}
      >
        <Button color="primary" component="span">
          <GetAppIcon style={{ transform: 'rotate(180deg)', fontSize: 20 }} />
          <span style={{ paddingLeft: '0.5em' }}>Import</span>
        </Button>
      </label>
    </>
  );
};

export default connect()(ImportButton);
