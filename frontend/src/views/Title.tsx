import React from 'react';

const Title = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', marginBottom:'10vh', alignItems: 'center' }}>
      <div
        style={{
          color: 'black',
          fontFamily: 'Bungee Hairline',
          fontSize: 'xxx-large',
          fontWeight: 'bold',
          height: '6rem',
          whiteSpace:'nowrap',
          marginTop:'7vh',
        }}
      >
        N E S H E F
      </div>
      <div
        style={{
          color: 'black',
          fontFamily: 'Bungee Hairline',
          fontSize: '1rem',
          fontWeight: 'bold',
          borderBottom:'solid 4px',
          backgroundColor:'#EBF3E9'
        }}
      >
        ALWAYS CLASSY, JUST A LITTLE BIT SASSY
      </div>
    </div>
  );
};

export default Title;
