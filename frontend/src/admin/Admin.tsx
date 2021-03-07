import React, { FC, useEffect } from 'react';
import { fetchUtils, Admin as ReactAdmin, Resource } from 'react-admin';
import simpleRestProvider from 'ra-data-simple-rest';
import authProvider from './authProvider';

import { UserList, UserEdit, UserCreate } from './Users';
import { CouponList, CouponEdit, CouponCreate } from './Coupons';
import { VendorList, VendorEdit, VendorCreate } from './Vendors';
import { CouponConfigCreate, CouponConfigEdit, CouponConfigList } from './CouponConfig';

const httpClient = (url: any, options: any) => {
  if (!options) {
    options = {};
  }
  if (!options.headers) {
    options.headers = new Headers({ Accept: 'application/json' });
  }
  const token = localStorage.getItem('token');
  options.headers.set('Authorization', `Bearer ${token}`);
  return fetchUtils.fetchJson(url, options);
};

export const Admin: FC = () => {
  const dataProvider = simpleRestProvider('api/v1', httpClient);
useEffect(()=>{
	let e=document.getElementById('root')
	e!.style.direction='ltr';
},[])

  return (
    <ReactAdmin style={{direction: 'ltr'}}  dataProvider={dataProvider} authProvider={authProvider}>
      {(permissions: 'admin' | 'user') => [
        permissions === 'admin' ? (
          <Resource
            name="users"
            list={UserList}
            edit={UserEdit}
            create={UserCreate}
          />
        ) : null,
        permissions === 'admin' ? (
          <Resource
            name="coupons"
            list={CouponList}
            edit={CouponEdit}
            create={CouponCreate}
          />
        ) : null,
        permissions === 'admin' ? (
          <Resource
            name="vendors"
            list={VendorList}
            edit={VendorEdit}
            create={VendorCreate}
          />
        ) : null,
        permissions === 'admin' ? (
          <Resource
            name="coupon_config"
            list={CouponConfigList}
            edit={CouponConfigEdit}
            create={CouponConfigCreate}
          />
        ) : null,
      ]}
    </ReactAdmin>
  );
};
