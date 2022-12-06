import pandas as pd
import datetime as dt
import matplotlib.dates as matdates
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str):
    if date_str[-8:-6] != '24':
        date_pd = pd.to_datetime(date_str)
    else:
        date_str = date_str[0:-8] + '00' + date_str[-6:]
        date_pd = pd.to_datetime(date_str) + dt.timedelta(days=1)
    return date_pd

def plot_1D_results(output_paths, plot_column_name,
                    y_axis_title, plot_title):
    fig, axs = plt.subplots(1, 1, figsize=(20, 10))
    fontsize = 20
    for data in output_paths.keys():
        this_path = output_paths[data]
        this_df = pd.read_csv(this_path)
        this_df['Date/Time'] = '2002' + this_df['Date/Time']
        this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
        data_st_date = this_df['Date/Time'].iloc[0]
        data_ed_date = this_df['Date/Time'].iloc[-1]
        data_list = this_df['Date/Time']
        this_y = this_df[plot_column_name].values
        axs.plot(data_list, this_y,
                 alpha=0.7,
                 linestyle='-',
                 linewidth=2,
                 label=data)

        datetime_ax_loc = matdates.HourLocator()
        datetime_ax_fmt = matdates.DateFormatter('%H:%M')
        axs.xaxis.set_major_locator(datetime_ax_loc)
        axs.xaxis.set_major_formatter(datetime_ax_fmt)
        for tick in axs.xaxis.get_major_ticks():
            tick.label.set_fontsize(fontsize * 0.8)
        for tick in axs.yaxis.get_major_ticks():
            tick.label.set_fontsize(fontsize * 0.8)
        axs.tick_params('x', labelrotation=45)
        axs.set_xlabel('Time (%s to %s)' % (data_st_date, data_ed_date), fontsize=fontsize)
        axs.set_ylabel(y_axis_title, fontsize=fontsize)
        axs.yaxis.get_offset_text().set_fontsize(fontsize * 0.7)
        axs.legend(loc='upper left', fontsize=10)
        plt.title(plot_title, fontsize=25)
        plt.tight_layout()
        plt.savefig('./param_exp_1/plot.png')

def get_2D_results(output_paths):
    max_y = 0
    p_o = 0
    for data in output_paths.keys():
        this_path = output_paths[data]
        this_df = pd.read_csv(this_path)
        this_y = this_df['ZONE ONE:Zone Mean Air Temperature [C](TimeStep) '].mean()
        if this_y > max_y:
            max_y = this_y
            p_o = data
    return p_o, max_y
