Summary:	Unicode character map
Summary(pl):	Mapa znaków unikodowych
Name:		gucharmap
Version:	1.5.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gucharmap/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	7ae1df29812ac27379858ffc02cfc318
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.6.3
BuildRequires:	intltool
BuildRequires:	libgnome-devel >= 2.10.0
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	/sbin/ldconfig
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
Requires:	gtk+2-devel >= 2:2.6.3
Requires:	libgnomeui-devel >= 2.10.0-2
Requires:	pango-devel >= 1:1.8.0

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

%build
gnome-doc-prepare --copy --force
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%scrollkeeper_update_post

%postun
/sbin/ldconfig
%scrollkeeper_update_postun

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
