# unpackaged:
# /usr/lib*/alsa-lib/libasound_module_ctl_arcam_av.so
# /usr/lib*/alsa-lib/libasound_module_pcm_usb_stream.so
#
Summary:	Advanced Linux Sound Architecture - plugins
Name:		alsa-plugins
Version:	1.0.28
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	6fcbbb31e96f8ebc5fb926184a717aa4
Source1:	%{name}-jack.conf
Source2:	%{name}-samplerate.conf
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	jack-audio-connection-kit-devel
#BuildRequires:	libav-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	pkg-config
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALSA plugins.

%package a52
Summary:	A52 output plugin for ALSA
Group:		Libraries

%description a52
A52 output plugin for ALSA.

%package jack
Summary:	JACK <--> ALSA PCM plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jack-audio-connection-kit >= 0.98

%description jack
This plugin converts the ALSA API over JACK (Jack Audio Connection
Kit) API. ALSA native applications can work transparently together
with jackd for both playback and capture.

%package lavcrate
Summary:	libavcodec-based rate converter plugin for ALSA
Group:		Libraries

%description lavcrate
libavcodec-based rate converter plugin for ALSA.

%package mix
Summary:	Up/down mixing plugins for ALSA
Group:		Libraries

%description mix
Up/down mixing plugins for ALSA.

%package pulse
Summary:	Up/down mixing plugins for PulseAudio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pulseaudio

%description pulse
Up/down mixing plugins for PulseAudio.

%package samplerate
Summary:	libsamplerate-based rate converter plugin for ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description samplerate
libsamplerate-based rate converter plugin for ALSA.

%package speexrate
Summary:	speex-based rate converter plugin for ALSA
License:	BSD
Group:		Libraries

%description speexrate
speex-based rate converter plugin for ALSA.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-avcodec
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/alsa/alsa.conf.d/50-jack.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/alsa/alsa.conf.d/10-samplerate.conf

mv $RPM_BUILD_ROOT%{_datadir}/alsa/alsa.conf.d/99-pulseaudio-default.conf{.example,}

rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_ctl_dsp_ctl.so
rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_ctl_oss.so
rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_pcm_alsa_dsp.so
rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/libasound_module_pcm_oss.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/alsa/alsa.conf.d

%files jack
%defattr(644,root,root,755)
%doc doc/README-jack
%{_datadir}/alsa/alsa.conf.d/50-jack.conf
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_jack.so

%if 0
%files a52
%defattr(644,root,root,755)
%doc doc/a52.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_a52.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_usb_stream.so

%files lavcrate
%defattr(644,root,root,755)
%doc doc/lavcrate.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_fast.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_faster.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_high.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_lavcrate_higher.so
%endif

%files mix
%defattr(644,root,root,755)
%doc doc/{upmix,vdownmix}.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_upmix.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_vdownmix.so

%files pulse
%defattr(644,root,root,755)
%doc doc/README-pulse
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_conf_pulse.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_ctl_pulse.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_pulse.so
%{_datadir}/alsa/alsa.conf.d/50-pulseaudio.conf
%{_datadir}/alsa/alsa.conf.d/99-pulseaudio-default.conf

%files samplerate
%defattr(644,root,root,755)
%doc doc/samplerate.txt
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_best.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_linear.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_medium.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_samplerate_order.so
%{_datadir}/alsa/alsa.conf.d/10-samplerate.conf

%files speexrate
%defattr(644,root,root,755)
%doc doc/speex*
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_pcm_speex.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_speexrate.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_speexrate_best.so
%attr(755,root,root) %{_libdir}/alsa-lib/libasound_module_rate_speexrate_medium.so

