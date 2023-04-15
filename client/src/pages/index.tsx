import Head from 'next/head';
import Image from 'next/image';
import { Inter } from 'next/font/google';
import styles from '@/styles/Home.module.css';
import Appbar from '@/components/Appbar';
import { Box } from '@mui/material';
import * as React from 'react';
import { Typography } from '@mui/material';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Donut from '@/components/Donut';

const inter = Inter({ subsets: ['latin'] });

const assets = [
  {
    value: 'JCI',
    label: 'JCI',
  },
  {
    value: 'TGT',
    label: 'TGT',
  },
  {
    value: 'CMCSA',
    label: 'CMCSA',
  },
  {
    value: 'CPB',
    label: 'CPB',
  },
  {
    value: 'MO',
    label: 'MO',
  },
  {
    value: 'APA',
    label: 'APA',
  },
  {
    value: 'MMC',
    label: 'MMC',
  },
  {
    value: 'MMC',
    label: 'MMC',
  },
  {
    value: 'JPM',
    label: 'JPM',
  },
  {
    value: 'ZION',
    label: 'ZION',
  },
  {
    value: 'PSA',
    label: 'PSA',
  },
  {
    value: 'BAX',
    label: 'BAX',
  },
  {
    value: 'BMY',
    label: 'BMY',
  },
  {
    value: 'LUV',
    label: 'LUV',
  },
  {
    value: 'PCAR',
    label: 'PCAR',
  },
  {
    value: 'TXT',
    label: 'TXT',
  },
  {
    value: 'TMO',
    label: 'TMO',
  },
  {
    value: 'DE',
    label: 'DE',
  },
  {
    value: 'MSFT',
    label: 'MSFT',
  },
  {
    value: 'HPQ',
    label: 'HPQ',
  },
  {
    value: 'SEE',
    label: 'SEE',
  },
  {
    value: 'VZ',
    label: 'VZ',
  },
  {
    value: 'CNP',
    label: 'CNP',
  },
  {
    value: 'NI',
    label: 'NI',
  },
  {
    value: 'T',
    label: 'T',
  },
];

export default function Home() {
  const [company, setCompany] = React.useState<string>('Apple');

  const handleChange = (event: SelectChangeEvent) => {
    setCompany(event.target.value as string);
  };
  return (
    <>
      <Head>
        <title>Arcana</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <div>
          <Appbar />
          <Box sx={{ m: 1, p: 1 }}>
            <Typography variant="h6" sx={{ mt: 1, textAlign: 'center' }}>
              Company/stock
            </Typography>
            <FormControl sx={{ mt: 2 }} variant="standard" fullWidth>
              <Select value={'CNP'} name="company" onChange={handleChange}>
                {assets.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
          <Box sx={{ display: 'flex', m: 1 }}>
            <Box sx={{ m: 1 }}>
              <Donut />
            </Box>
            <Box sx={{ m: 1 }}>
              <Donut />
            </Box>
          </Box>
        </div>
      </main>
    </>
  );
}
