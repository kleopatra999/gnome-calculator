Summary:	GNOME calculator
Summary(pl):	Kalkulator dla GNOME
Name:		gcalctool
Version:	5.5.29
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/5.5/%{name}-%{version}.tar.bz2
# Source0-md5:	ba52db243366d2693344b02daf581e39
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	atk-devel >= 1.5.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	scrollkeeper
Requires(post):	/usr/bin/scrollkeeper-update
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcalctool is a simple calculator that performs a variety of functions.

%description -l pl
gcalctool jest prostym kalkulatorem spełniającym wiele funkcji.

%prep
%setup -q
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS gcalctoolrc NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_mandir}/man1/*
