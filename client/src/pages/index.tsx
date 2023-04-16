import Head from 'next/head';
import * as React from 'react';
import { useState } from 'react';
import Image from 'next/image';
import { Inter } from 'next/font/google';
import styles from '@/styles/Home.module.css';
import Appbar from '@/components/Appbar';
import { Box } from '@mui/material';
import { Typography } from '@mui/material';
import { Button } from '@mui/material';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import CircularProgress from '@mui/material/CircularProgress';

//Plots
import Donut from '@/components/Donut';
import Histogram from '@/components/Histogram';

//axios
import axios from 'axios';

//date
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import dayjs, { Dayjs } from 'dayjs';

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
  const [startDate, setStartDate] = useState<Dayjs | null>(dayjs('2019-01-01'));
  const [endDate, setEndDate] = useState<Dayjs | null>(dayjs('2022-12-31'));
  const [loading, setLoading] = useState<boolean>(false);

  //Plots
  const [Plot1, setPlot1] = React.useState<any>(null);
  const [Plot2, setPlot2] = React.useState<any>(null);
  const [Plot3, setPlot3] = React.useState<any>(null);
  const [Plot4, setPlot4] = React.useState<any>(null);
  const [Plot5, setPlot5] = React.useState<any>(null);
  const [Plot6, setPlot6] = React.useState<any>(null);
  const [Plot7, setPlot7] = React.useState<any>(null);
  const [Plot8, setPlot8] = React.useState<any>(null);
  const [Plot9, setPlot9] = React.useState<any>(null);

  const [company, setCompany] = React.useState<string>('JCI');
  const [summary, setSummary] = React.useState<any>(null);
  const [name, setName] = React.useState<any>(null);
  const [sector, setSector] = React.useState<any>(null);
  const [industry, setIndustry] = React.useState<any>(null);

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log('submit');
    console.log(company);

    console.log(startDate?.format('YYYY-MM-DD'));
    console.log(endDate);

    if (startDate && endDate && startDate > endDate) {
      alert('Start date cannot be greater than end date');
      return;
    }

    setLoading(true);

    axios
      .post(
        `http://localhost:5000/image`,
        {
          company: company,
          start: startDate?.format('YYYY-MM-DD'),
          end: endDate?.format('YYYY-MM-DD'),
        },
        {
          headers: {
            // 'Content-Type': 'multipart/form-data',
            'Content-Type': 'application/json',
          },
        }
      )
      .then((res) => {
        console.log(res.data);
        setSummary(res.data.summary);
        setName(res.data.name);
        setSector(res.data.sector);
        setIndustry(res.data.industry);
        setPlot1('data:image/png;base64,' + res.data.plot1.toString('base64'));
        setPlot2('data:image/png;base64,' + res.data.plot2.toString('base64'));
        setPlot3('data:image/png;base64,' + res.data.plot3.toString('base64'));
        setPlot4('data:image/png;base64,' + res.data.plot4.toString('base64'));
        setPlot5('data:image/png;base64,' + res.data.plot5.toString('base64'));
        setPlot6('data:image/png;base64,' + res.data.plot6.toString('base64'));
        setPlot7('data:image/png;base64,' + res.data.plot7.toString('base64'));
        setPlot8('data:image/png;base64,' + res.data.plot8.toString('base64'));
        setLoading(false);
      });
  };

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
        <Box>
          <Appbar />
          <Box sx={{ m: 1, p: 1 }}>
            <Typography sx={{ mt: 1 }}>Company/stock</Typography>
            <FormControl
              component="form"
              onSubmit={handleSubmit}
              // variant="standard"
              fullWidth
            >
              <Select value={company} name="company" onChange={handleChange}>
                {assets.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </Select>
              <Box sx={{ display: 'flex' }}>
                <Box sx={{ p: 1 }}>
                  <Typography sx={{ mt: 1 }}>Start Date</Typography>
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <DatePicker
                      onChange={(newValue) => setStartDate(newValue)}
                      value={startDate}
                    />
                  </LocalizationProvider>
                </Box>
                <Box sx={{ p: 1 }}>
                  <Typography sx={{ mt: 1 }}>End Date </Typography>
                  <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <DatePicker
                      onChange={(newValue) => setEndDate(newValue)}
                      value={endDate}
                    />
                  </LocalizationProvider>
                </Box>
              </Box>

              <Box sx={{ p: 1 }}>
                <Button type="submit" variant="contained">
                  Submit
                </Button>
              </Box>
            </FormControl>
          </Box>
          {/* <Box sx={{ display: 'flex', m: 1 }}>
            <Box sx={{ m: 1 }}>
              <Donut />
            </Box>
            <Box sx={{ m: 1 }}>
              <Donut />
            </Box>
            <Box>
              <Histogram />
            </Box>
          </Box> */}
          {loading && (
            <Box sx={{ display: 'flex', justifyContent: 'center' }}>
              <CircularProgress />
            </Box>
          )}
          {!loading && (
            <Box>
              <Box
                sx={{
                  display: 'flex',
                  m: 1,
                  flexDirection: 'column',
                  alignItems: 'center',
                }}
              >
                {Plot1 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot1} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot2 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot2} alt="plot" width={800} height={500} />
                  </Box>
                )}

                {Plot5 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot5} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot6 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot6} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot7 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot7} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot8 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot8} alt="plot" width={800} height={500} />
                  </Box>
                )}

                {Plot3 && (
                  <Box sx={{ mt: 1 }}>
                    <Image src={Plot3} alt="plot" width={800} height={500} />
                  </Box>
                )}
                {Plot4 && (
                  <Box sx={{ m: 1 }}>
                    <Image src={Plot4} alt="plot" width={800} height={500} />
                  </Box>
                )}
              </Box>
            </Box>
          )}
        </Box>
      </main>
    </>
  );
}
