Summary:	Unicode character map
Summary(pl):	Mapa znaków unikodowych
Name:		gucharmap
Version:	1.3.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	6e2f4d22436d009382e71ae593f11f74
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.3.0
BuildRequires:	gtk+2-devel >= 2.2.4
BuildRequires:	libgnome-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.5
BuildRequires:	popt-devel
BuildRequires:  scrollkeeper >= 0.3.8
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gucharmap is a featureful unicode character map.

%description -l pl
Gucharmap jest warto¶ciow± map± znaków unikodowych.

%package devel
Summary:	Headers for gucharmap
Summary(pl):	Pliki nag³ówkowe gucharmap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2.2.4
Requires:	libgnomeui-devel >= 2.4.0
Requires:	pango-devel >= 1.2.5

%description devel
The gucharmap-devel package includes the header files that you will
need to use gucharmap.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji programów
u¿ywaj±cych gucharmap.

%package static
Summary:	Static gucharmap libraries
Summary(pl):	Statyczne biblioteki gucharmap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of gucharmap libraries.

%description static -l pl
Statyczna wersja bibliotek gucharmap.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf gucharmap $RPM_BUILD_ROOT%{_bindir}/charmap

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*charmap
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
