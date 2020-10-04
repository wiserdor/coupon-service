//@ts-nocheck
import React from 'react';
import Button from '@material-ui/core/Button';
import GetAppIcon from '@material-ui/icons/GetApp';
import { connect } from 'react-redux';
import { parse as convertFromCSV } from 'papaparse';
import { crudUpdateMany } from 'ra-core';

const ImportButton = (props: any) => {
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

                    const values = data.slice(1).map(row => {
                        const value: any = {};

                        keys.forEach((key, index) => {
                            value[key] = row[index];
                        });

                        return value;
                    });

                    const ids = values.map(v => v[primaryKey]);
                    dispatch(
                        crudUpdateMany(resource, ids, values, basePath)
                    );
                }
            });
        }
    };

    return (
        <>
            <input
                type="file"
                id="text-button-file"
                style={{ display: 'none' }}
                accept='.csv'
                onChange={handleChange}
            />
            <label htmlFor="text-button-file" style={{ display: 'inline-flex', alignItems: 'center' }}>
                <Button
                    color="primary"
                    component="span"
                >
                    <GetAppIcon style={{ transform: 'rotate(180deg)', fontSize: 20 }} />
                    <span style={{ paddingLeft: '0.5em' }}>Import</span>
                </Button>
            </label>
        </>
    );
};

export default connect()(ImportButton);